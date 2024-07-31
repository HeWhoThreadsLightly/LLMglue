from ChatHistory import ChatHistory
from LLMglue.GlueLadder import GlueLadder
from LLMglue.GlueModule import GlueModule


class ModuleToT(GlueModule):
    def __init__(self, ladder: GlueLadder, index: int):
        super().__init__(ladder, index)
        self.model = super().getGlueModel()  # get a reference to the next model for prompting

    def prompt(self, **kwargs):
        pass  # todo make an message list that prompts are appended to

    def solve(self, method_generate, task, idx, to_print=True):

        x = task.get_input(idx)  # input
        ys = ['']  # current output candidates
        infos = []
        for step in range(task.steps):
            # generation
            if args.method_generate == 'sample':
                new_ys = [get_samples(task, x, y, args.n_generate_sample, prompt_sample=args.prompt_sample,
                                      stop=task.stops[step]) for y in ys]
            elif args.method_generate == 'propose':
                new_ys = [get_proposals(task, x, y) for y in ys]
            new_ys = list(itertools.chain(*new_ys))
            ids = list(range(len(new_ys)))
            # evaluation
            if args.method_evaluate == 'vote':
                values = get_votes(task, x, new_ys, args.n_evaluate_sample)
            elif args.method_evaluate == 'value':
                values = get_values(task, x, new_ys, args.n_evaluate_sample)

            # selection
            if args.method_select == 'sample':
                ps = np.array(values) / sum(values)
                select_ids = np.random.choice(ids, size=args.n_select_sample, p=ps).tolist()
            elif args.method_select == 'greedy':
                select_ids = sorted(ids, key=lambda x: values[x], reverse=True)[:args.n_select_sample]
            select_new_ys = [new_ys[select_id] for select_id in select_ids]

            # log
            if to_print:
                sorted_new_ys, sorted_values = zip(*sorted(zip(new_ys, values), key=lambda x: x[1], reverse=True))
                print(
                    f'-- new_ys --: {sorted_new_ys}\n-- sol values --: {sorted_values}\n-- choices --: {select_new_ys}\n')

            infos.append(
                {'step': step, 'x': x, 'ys': ys, 'new_ys': new_ys, 'values': values, 'select_new_ys': select_new_ys})
            ys = select_new_ys

        if to_print:
            print(ys)
        return ys, {'steps': infos}

    def message(self, history: ChatHistory):
        # TODO run the TOT algorithm to generate the next response
        # TOT algorithm generate continuations, vote on the continuations pick the continuation with the highest score.

        history.copy()
        raise NotImplemented
    def start(self):
        raise NotImplemented
        try:
            while True:                     # loop until keyboard interrupt
                prompt = input()                 # get user input
                self.history.add_message(prompt)
                r = self.model.message(self.history)  # send input to next module
                self.history.print()
                print(r)                    # print the model response
        except KeyboardInterrupt:
            print('interrupted!')


if __name__ == "__main__":
    from ModuleSimpleUI import ModuleSimpleUI
    from ModuleOpenAI import ModuleOpenAI
    configuration = [ModuleSimpleUI(None, 0), ModuleToT(None, 1), ModuleOpenAI(None, 2)]
    ladder = GlueLadder(configuration)  # use default example configuration
    ladder.start()
