import pygad
import numpy

desired_output = 59


def fitness_func(solution, solution_idx):
    output = numpy.sum(solution * function_inputs)
    fitness = 1.0 / numpy.abs(output - desired_output)
    return fitness


function_inputs = [0, 2, 3, 4, 1, 84]


params = dict(
    fitness_func=fitness_func,
    num_generations=999,
    num_parents_mating=4,
    sol_per_pop=8,
    num_genes=len(function_inputs),
    init_range_low=-2,
    init_range_high=5,
    parent_selection_type="sss",
    keep_parents=1,
    crossover_type="single_point",
    mutation_type="random",
    mutation_percent_genes=10,
)

print(params)

ga_instance = pygad.GA(**params)

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()

print("Parameters of the best solution : {solution}".format(solution=solution))
print(
    "Fitness value of the best solution = {solution_fitness}".format(
        solution_fitness=solution_fitness
    )
)

prediction = numpy.sum(numpy.array(function_inputs) * solution)
print(
    "Predicted output based on the best solution : {prediction}".format(
        prediction=prediction
    )
)
