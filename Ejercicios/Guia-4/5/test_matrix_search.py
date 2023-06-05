from matrix_search import MatrixSearch

class TestMatrixSearch:
    def test_search_matrix(self):
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60]
        ]
        target = 16

        searcher = MatrixSearch()
        result = searcher.search_matrix(matrix, target)

        assert result == True

