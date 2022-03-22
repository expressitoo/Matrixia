class Matrix:
    def __init__(self, *argv) -> None:
        self.emptyMatrix = []
        self.identity = []

    def createEmpty(self, n: int, p: int) -> list:
        """
        Prend en argument n, un nombre de lignes et p, un nombre de colonnes et retourne un matrice vide.
        """

        self.emptyMatrix = [[0 for columns in range(p)] for lines in range(n)]

        return self.emptyMatrix

    def Identity(self, n) -> list:
        """
        Prend en argument n, la taille d'une matrice carrée et retourne la matrice identité.
        """

        self.identity = self.createEmpty(n, n)

        for lines in range(0, n):
            self.identity[lines][lines] = 1
            
        return self.identity

    def checkSquare(self, matrix: list):
        """
        Vérifie si la matrice passée en argument est une matrice carrée.
        """
        
        lines = len(matrix)
        
        for column in matrix:
            if len(column) != lines : return False

        return True

    def add(self, matrixA: list, matrixB: list):
        """
        Prend deux matrices en argument et retourne le résultat de l'addition de ces deux matrices.
        """

        assert self.checkSquare(matrixA), "Matrix need to have same number of lines as columns"
        assert self.checkSquare(matrixB), "Matrix need to have same number of lines as columns"

        size = self.getNumberOfLines(matrixA)
        imageMatrix = self.createEmpty(size, size)

        imagePrecompute = [valueA + valueB for mtA, mtB in zip(matrixA, matrixB) for valueA, valueB in zip(mtA, mtB)]

        for width in range(size):
            for depth in range(size):
                imageMatrix[width][depth] = imagePrecompute[0]
                imagePrecompute.pop(0)
        
        return imageMatrix

    def sub(self, matrixA: list, matrixB: list):
        """
        Prend deux matrices en argument et retourne le résultat de la soustraction de ces deux matrices.
        """

        assert self.checkSquare(matrixA), "Matrix need to have same number of lines as columns"
        assert self.checkSquare(matrixB), "Matrix need to have same number of lines as columns"

        size = self.getNumberOfLines(matrixA)
        imageMatrix = self.createEmpty(size, size)

        imagePrecompute = [valueA - valueB for mtA, mtB in zip(matrixA, matrixB) for valueA, valueB in zip(mtA, mtB)]

        for width in range(size):
            for depth in range(size):
                imageMatrix[width][depth] = imagePrecompute[0]
                imagePrecompute.pop(0)
        
        return imageMatrix

    def mul(self, matrixA: list, matrixB: list):
        """
        Prend deux matrices en argument et retourne le résultat de la multiplication de ces deux matrices.
        """

        assert self.getNumberOfColumns(matrixA) == self.getNumberOfLines(matrixB), "Matrix A's columns needs to be equal to matrix B's lines"
        sizeA = len(matrixA)
        sizeB = len(matrixB)
        
        imageMatrix = self.createEmpty(sizeA, sizeA)

        index = 0

        for mtA in matrixA:
            print(mtA,"--")
            for times in range(len(matrixB[0])):
                value_to_write = 0
                for i in range(sizeB):
                    value_to_write += mtA[i] * matrixB[i][times]
                imageMatrix[index][times] = value_to_write
            index += 1
        
        return imageMatrix

    def scalarMul(self, matrix: list, scalar: int):
        """
        Compute scalar multiplication of the matrix given as parameter with the scalar.
        """

        assert self.checkValid(matrix), "Not a valid matrix"

        size = len(matrix[0])

        for line in range(len(matrix)):
            for column in range(size):
                matrix[line][column] *= scalar

        return matrix

    def changeValue(self, matrix: list, i: int, j: int, value: int) -> None:
        """
        Change the value at a position (i, j) in the matrix given as parameter.
        """

        assert (i <= len(matrix) - 1) and (j <= len(matrix) - 1), "Bad indexes"
        matrix[i][j] = value

    def getNumberOfLines(self, matrix: list) -> int:
        """
        Retourne le nombre de lignes de la matrice passée en argument.
        """

        return len(matrix)

    def getNumberOfColumns(self, matrix: list) -> int:
        """
        Retourne le nombre de colonnes de la matrice passée en argument.
        """

        self.checkValid(matrix)

        return len(matrix[0])

    def checkValid(self, matrix: list) -> bool:
        """
        Vérifie si une matrice est valide (le nombre de colonnes n'est pas différent sur une ligne).
        """

        size = len(matrix[0])

        for line in matrix:
            if len(line) != size: return False

        return True

    def beautify(self, matrix: list) -> str:
        """
        Renvoie une matrice passée en argument sous forme de string. 
        """
        
        return str(matrix).replace("],", "],\n")