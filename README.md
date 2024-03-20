# LLMglue
Glue logic for LLM addons. Part of thesis work to conect User->ChatDev->ToT->MemGPT->LLM together in a atempt to improve maximum project size. ChatDev will be modified to be able to make use of MemGpt to improve LLM memory, and ToT to improve LLM reasoning ability. Different permutations of improvements MemGpt, ToT, and LLM versions gpt3.5-turbo-16k, gpt-4-0125-preview, or gpt-4-1106-preview for a total of 12 combinations. Twelve different configurations of ChatDev will undergo experimental testing on a set of projects to analyze the impact of different parameters on cost, project size, and development time.
![Base module use case and components](Assets/OriginalModule.drawio.svg)
Normal use case and common components of the original ChatDev, ToT, MemGpt calling to OpenAI for cloud LLM compute. ChatDev, ToT, and MemGpt are colectivly reffered to as *modules* in this text.

The module user interface and LLM API call is replaced with glue logic code to call the next module in the configuration, the UI of ChatDev is not replaced as the module is common to all configurations instead of creating a separate UI node.
![Multiple modules conected with glue lodgic](Assets/GlueComponent.drawio.svg)
Illustration of glue logic with the modified ToT expanded to show the replaced UI and LLM API.

## Instalation instructions
  1. Clone this repository `git clone --recurse-submodules https://github.com/HeWhoThreadsLightly/LLMglue.git`
  2. Open the downloaded repository `cd LLMglue`
  3. Setup conda `conda create -n LLMglue python=3.10`
  4. Activate the conda enviroment `conda activate LLMglue`
  5. Install dependencies `pip3 install -r requirements.txt`
