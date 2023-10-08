# class Worker:
#
#     def __init__(self, name, salary, energy):
#         self.name = name
#         self.salary = salary
#         self.energy = energy
#         self.money = 0
#
#     def work(self):
#         if self.energy <= 0:
#             raise Exception('Not enough energy.')
#
#         self.money += self.salary
#         self.energy -= 1
#
#     def rest(self):
#         self.energy += 1
#
#     def get_info(self):
#         return f'{self.name} has saved {self.money} money.'
#

from unittest import TestCase, main


class WorkerTests(TestCase):
    def test_worker_is_initialized_with_correct_name(self):
        worker = Worker("Test", 100, 10)
        self.assertEqual("Test", worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy)

    def test_is_worker_energy_incremented_correctly(self):
        worker = Worker("Test", 100, 10)
        worker.rest()
        self.assertEqual(11, worker.energy)

    def test_an_error_is_raised_when_worker_is_trying_to_work_with_negative_energy(self):
        worker = Worker("Test", 100, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

        worker = Worker("Test", 100, -1)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_if_the_worker_salary_is_incremented_properly(self):
        worker = Worker("Test", 100, 10)
        worker.work()
        self.assertEqual(100, worker.money)

    def test_if_the_workers_energy_is_decreased_correctly(self):
        worker = Worker("Test", 100, 10)
        worker.work()
        self.assertEqual(9, worker.energy)

    def test_if_the_get_info_method_works_correctly(self):
        worker = Worker("Test", 100, 10)
        worker.work()
        expected = 'Test has saved 100 money.'
        self.assertEqual(expected, worker.get_info())


if __name__ == '__main__':
    main()