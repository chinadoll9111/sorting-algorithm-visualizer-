from algorithms import Algorithms

class Controller:
    def __init__(self):
        self.algorithms = Algorithms()
        self.algorithm = None

    def set_algorithm(self, algorithm_name):
        """Set the sorting algorithm based on dropdown selection."""
        if algorithm_name == "Bubble Sort":
            self.algorithm = self.algorithms.bubble_sort
        elif algorithm_name == "Selection Sort":
            self.algorithm = self.algorithms.selection_sort
        elif algorithm_name == "Insertion Sort":
            self.algorithm = self.algorithms.insertion_sort
        elif algorithm_name == "Merge Sort":
            self.algorithm = self.algorithms.merge_sort
        elif algorithm_name == "Quick Sort":
            self.algorithm = self.algorithms.quick_sort
        else:
            raise ValueError(f"Algorithm '{algorithm_name}' not recognized.")
