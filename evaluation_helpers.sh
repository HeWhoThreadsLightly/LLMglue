
test() {
    gnome-text-editor manual.md &
    conda remove --name tmp_env --all -y
    conda create --name tmp_env python=3.10 -y
    conda activate tmp_env
    conda install tk
    # pip install pygame --pre
    cat requirements.txt
    # pip install -r 'requirements.txt'
    
    local requirements_file="requirements.txt"

    if [[ ! -f "$requirements_file" ]]; then
        echo "File $requirements_file not found!"
        return 1
    fi

    while IFS= read -r requirement || [[ -n "$requirement" ]]; do
        if [[ ! -z "$requirement" && ! "$requirement" =~ ^# ]]; then
            echo "Installing $requirement..."
            pip3 install "$requirement" || echo "Failed to install $requirement, skipping..."
        fi
    done < "$requirements_file"
    python 'main.py'
    conda deactivate
}

# Global variables for binary search
export _bsearch_dirs=()
export _bsearch_low=0
export _bsearch_high=0
export _bsearch_mid=0
export _bsearch_last_passed=""

# Global variables for binary search
export _bsearch_dirs=()
export _bsearch_low=0
export _bsearch_high=0
export _bsearch_mid=0
export _bsearch_last_passed=""

benter() {
    # Populate the array with directory names, properly handling spaces and special characters
    mapfile -t _bsearch_dirs < <(ls -d -- *_req[0-9]* 2>/dev/null | sort -V)

    if [[ ${#_bsearch_dirs[@]} -eq 0 ]]; then
        echo "No directories ending in _req(n) found."
        return 1
    fi

    _bsearch_low=0
    _bsearch_high=$((${#_bsearch_dirs[@]} - 1))
    _bsearch_mid=$(( (_bsearch_low + _bsearch_high) / 2 ))
    _bsearch_last_passed=""

    cd "${_bsearch_dirs[$_bsearch_mid]}"
    echo "Starting binary search in directory: ${_bsearch_dirs[$_bsearch_mid]}"
}

bpass() {
    _bsearch_last_passed="${_bsearch_dirs[$_bsearch_mid]}"

    if [[ $_bsearch_low -eq $_bsearch_high ]]; then
        echo "No higher directories to search."
        cd "../$_bsearch_last_passed"
        echo "Ending search. Navigating to the highest passed directory: $_bsearch_last_passed"
        return 0
    fi

    _bsearch_low=$((_bsearch_mid + 1))

    if [[ $_bsearch_low -gt $_bsearch_high ]]; then
        echo "No higher directories to search."
        cd "../$_bsearch_last_passed"
        echo "Ending search. Navigating to the highest passed directory: $_bsearch_last_passed"
        return 0
    fi

    _bsearch_mid=$(( (_bsearch_low + _bsearch_high) / 2 ))

    cd "../${_bsearch_dirs[$_bsearch_mid]}"
    echo "Continuing in higher directory: ${_bsearch_dirs[$_bsearch_mid]}"
}

bfail() {
    if [[ $_bsearch_low -eq $_bsearch_high ]]; then
        echo "No lower directories to search."
        cd "../$_bsearch_last_passed"
        echo "Ending search. Navigating to the highest passed directory: $_bsearch_last_passed"
        return 0
    fi

    _bsearch_high=$((_bsearch_mid - 1))

    if [[ $_bsearch_high -lt $_bsearch_low ]]; then
        echo "No lower directories to search."
        cd "../$_bsearch_last_passed"
        echo "Ending search. Navigating to the highest passed directory: $_bsearch_last_passed"
        return 0
    fi

    _bsearch_mid=$(( (_bsearch_low + _bsearch_high) / 2 ))

    cd "../${_bsearch_dirs[$_bsearch_mid]}"
    echo "Continuing in lower directory: ${_bsearch_dirs[$_bsearch_mid]}"
}
