import unittest
from algorithms import calculate_factorial, is_prime

class TestAlgorithms(unittest.TestCase):
    def test_factorial_of_0(self):
        result = calculate_factorial(0)
        self.assertEqual(result, 1)

    def test_factorial_of_1(self):
        result = calculate_factorial(1)
        self.assertEqual(result, 1)

    def test_factorial_of_positive_number(self):
        result = calculate_factorial(5)
        self.assertEqual(result, 120)

    def test_factorial_of_negative_number(self):
        with self.assertRaises(ValueError):
            calculate_factorial(-3)

    # Exercice: 10
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(13))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(15))

    # Exercice 11
    def test_are_amicable_numbers(self):
        self.assertTrue(are_amicable_numbers(220, 284))
        self.assertTrue(are_amicable_numbers(1184, 1210))
        self.assertFalse(are_amicable_numbers(220, 285))
        self.assertFalse(are_amicable_numbers(1184, 1211))

    # Exercice 22
     def test_calculate_matrix_trace(self):
        result = calculate_matrix_trace(3, "1,2,3;4,5,6;7,8,9")
        self.assertEqual(result, 15)

        result = calculate_matrix_trace(2, "2,1;4,3")
        self.assertEqual(result, 5)

        with self.assertRaises(ValueError):
            calculate_matrix_trace(2, "2,1;4,3;6,5")

    # Exercice 23
    def test_calculate_transposed_matrix(self):
        result = calculate_transposed_matrix(2, "1,2;3,4")
        expected_result = [[1, 3], [2, 4]]
        self.assertEqual(result, expected_result)

        result = calculate_transposed_matrix(3, "1,2,3;4,5,6;7,8,9")
        expected_result = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        self.assertEqual(result, expected_result)

        with self.assertRaises(ValueError):
            calculate_transposed_matrix(2, "1,2;3,4;5,6")

    # Exercice 27
    def test_occurrences(self):
        result = occurrences(2, [1, 2, 3, 2, 4, 2])
        self.assertEqual(result, 3)

        result = occurrences('a', ['a', 'b', 'a', 'c', 'a', 'a'])
        self.assertEqual(result, 4)

    def test_concatener(self):
        result = concatener([1, 2, 3], [4, 5, 6])
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

        result = concatener(['a', 'b'], ['c', 'd'])
        self.assertEqual(result, ['a', 'b', 'c', 'd'])

    def test_recherche(self):
        result = recherche(3, [1, 2, 3, 4, 5])
        self.assertEqual(result, 2)

        result = recherche('b', ['a', 'b', 'c', 'd'])
        self.assertEqual(result, 1)

        result = recherche('x', ['a', 'b', 'c', 'd'])
        self.assertEqual(result, -1)

    # Exercice 31
     def test_update_ranking(self):
        runner1 = Runner(1, 'John', 120)
        runner2 = Runner(2, 'Alice', 110)
        runner3 = Runner(3, 'Bob', 130)
        runners = [runner1, runner2, runner3]

        result = update_ranking(runners)
        expected_result = [(2, 'Alice', 110), (1, 'John', 120), (3, 'Bob', 130)]
        self.assertEqual(result, expected_result)

    # Exercice 33: Eneo
    def test_add_client(self):
        queue = deque()
        client = Client(1, 'John', '08:30')
        add_client(queue, client)
        self.assertEqual(len(queue), 1)

        client = Client(2, 'Alice', '08:35')
        add_client(queue, client)
        self.assertEqual(len(queue), 2)

    def test_serve_next_client(self):
        queue = deque()
        client1 = Client(1, 'John', '08:30')
        client2 = Client(2, 'Alice', '08:35')

        add_client(queue, client1)
        add_client(queue, client2)

        result = serve_next_client(queue)
        self.assertEqual(result, "Client 1 (John)")

        result = serve_next_client(queue)
        self.assertEqual(result, "Client 2 (Alice)")

        result = serve_next_client(queue)
        self.assertEqual(result, "Aucun client en attente")
    
    # Exercice 34:
    def test_evaluate_expression(self):
        expression1 = "3 5 4 * + 2 *"
        result1 = evaluate_expression(expression1)
        self.assertEqual(result1, 42)

        expression2 = "10 2 /"
        result2 = evaluate_expression(expression2)
        self.assertEqual(result2, 5)

        expression3 = "1 2 + 3 * 4 -"
        result3 = evaluate_expression(expression3)
        self.assertEqual(result3, 9)

        expression4 = "5 0 /"
        with self.assertRaises(ValueError):
            evaluate_expression(expression4)

    # Exercice: 40
    def test_conjugate_verb(self):
        verb1 = "parler"
        result1 = conjugate_verb(verb1)
        expected1 = "Au présent : Je parle, Tu parles, Il/Elle/On parle, Nous parlons, Vous parlez, Ils/Elles parlent, Au futur : Je parlerai, Tu parleras, Il/Elle/On parlera, Nous parlerons, Vous parlerez, Ils/Elles parleront"
        self.assertEqual(result1, expected1)

        verb2 = "manger"
        result2 = conjugate_verb(verb2)
        expected2 = "Au présent : Je mange, Tu manges, Il/Elle/On mange, Nous mangeons, Vous mangez, Ils/Elles mangent, Au futur : Je mangerai, Tu mangeras, Il/Elle/On mangera, Nous mangerons, Vous mangerez, Ils/Elles mangeront"
        self.assertEqual(result2, expected2)

    # Exercice 41
     def test_selection_sort(self):
        input_list1 = "5,3,8,1,7"
        result1 = selection_sort(input_list1)
        expected1 = [1, 3, 5, 7, 8]
        self.assertEqual(result1, expected1)

        input_list2 = "10,5,2,8,12"
        result2 = selection_sort(input_list2)
        expected2 = [2, 5, 8, 10, 12]
        self.assertEqual(result2, expected2)

    # Exercice 42
    def test_insertion_sort(self):
        input_list1 = "5,3,8,1,7"
        result1 = insertion_sort(input_list1)
        expected1 = [1, 3, 5, 7, 8]
        self.assertEqual(result1, expected1)

        input_list2 = "10,5,2,8,12"
        result2 = insertion_sort(input_list2)
        expected2 = [2, 5, 8, 10, 12]
        self.assertEqual(result2, expected2)

    # Exercice 43
    def test_bubble_sort(self):
        input_list1 = "5,3,8,1,7"
        result1 = bubble_sort(input_list1)
        expected1 = [1, 3, 5, 7, 8]
        self.assertEqual(result1, expected1)

        input_list2 = "10,5,2,8,12"
        result2 = bubble_sort(input_list2)
        expected2 = [2, 5, 8, 10, 12]
        self.assertEqual(result2, expected2)

    # Exercice 44
    def test_element_at_position(self):
        input_list = "5,3,8,1,7"
        
        result1 = element_at_position(input_list, 2)
        expected1 = 8
        self.assertEqual(result1, expected1)

        result2 = element_at_position(input_list, 0)
        expected2 = 5
        self.assertEqual(result2, expected2)

        result3 = element_at_position(input_list, 5)
        expected3 = None
        self.assertEqual(result3, expected3)

    # Exercice 45
    def test_add_element_at_position(self):
        # Création d'une liste chaînée 5 -> 3 -> 8 -> 1 -> 7
        head = Node(5)
        head.next = Node(3)
        head.next.next = Node(8)
        head.next.next.next = Node(1)
        head.next.next.next.next = Node(7)

        result1 = add_element_at_position(head, 10, 2)
        expected1 = [5, 3, 10, 8, 1, 7]
        self.assertEqual(self.get_linked_list_values(result1), expected1)

        result2 = add_element_at_position(head, 4, 0)
        expected2 = [4, 5, 3, 8, 1, 7]
        self.assertEqual(self.get_linked_list_values(result2), expected2)

        result3 = add_element_at_position(head, 9, 5)
        expected3 = [5, 3, 8, 1, 7, 9]
        self.assertEqual(self.get_linked_list_values(result3), expected3)

    def get_linked_list_values(self, head):
        values = []
        current = head
        while current:
            values.append(current.value)
            current = current.next
        return values


if __name__ == '__main__':
    unittest.main()
