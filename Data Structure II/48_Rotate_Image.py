class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Start with the outer most layer / row & columns i.e. row[0], row[N-1] & columns[0], columns[N-1]
        # iteratively go inwards. At each layer ~ notice that the i'th element in 0 row becomes the
        # ith element in N-1'th column, wimilary i'th element in N-1 column becomes N-i'th elements in N-1 row
        # essentially there's a cycle across the layer for each of the elements
        # We need to swap each element in consecutive changed positions.

        N = len(matrix)
        endDim = N-2 if N%2 else N-1
 
        # consider the lth layer which is initialized as the outer most layer i.e. 0
        l = 0
        # how many layers ? ~>> len(matrix)-2 number of layers
        # this layer will have N-2l rows & N-2l columns indices from l to N-l
        
        while l < endDim:
            
            for i in range(l, N-l-1):
                # print(i, l)
                # iterate through all elements in l'th row
                # and transition: 
                #
                #   - (l+i)th element in lth row to the (l+i)th element in (N-l)th column 
                #   - the (l+i)th element in (N-l)th column to the (N-l-i)th element in (N-l)th column
                #   - the (N-l-i)th element in (N-l)th column to the (N-l-i)th elemnt in lth column
                #   - the (N-l-i)th element in lth column to ith element in lth row
                #
                # swap respective elements in specified order 
                # NOTE: ['l +' bit of indices is already considers in for loop traversal]

                # Swap the ith element from lth row i.e. l in between l and N-l-1 (inclusive)
                # with the ith elemnt in the N-lth row i.e. index wise N-l-1
                tmp = matrix[i][N-l-1]; # print("{} -> {}".format(matrix[l][i], matrix[i][N-l-1]))
                matrix[i][N-l-1] = matrix[l][i]
                
                # swap ith element in N-l-1 column with the N-1-l-i'th elemnt in N-l-1 row
                cIdx = N-1-l-i if l == 0 else N-1-i # handle corner case when 1 < l
                # tmp2 = matrix[N-l-1][N-l-1-i]; print("{} -> {}".format(tmp, matrix[N-l-1][N-l-1-i]))
                # matrix[N-l-1][N-l-1-i] = tmp
                tmp2 = matrix[N-l-1][cIdx]; # print("{} -> {}".format(tmp, matrix[N-l-1][cIdx]))
                matrix[N-l-1][cIdx] = tmp
                tmp = tmp2

                # swap the N-l-1-i'th element in N-l-i row with the N-l-1-i'th element in lth column
                rIdx = N-1-l-i if l == 0 else N-1-i # handle corner case when 1 < l
                # tmp2 = matrix[N-1-l-i][l]; print("{} -> {}".format(tmp, matrix[N-1-l-i][l]))
                # matrix[N-1-l-i][l] = tmp
                tmp2 = matrix[rIdx][l]; # print("{} -> {}".format(tmp, matrix[rIdx][l]))
                matrix[rIdx][l] = tmp
                tmp = tmp2

                # swap the N-1-l-i'th element in lth column with ith element in lth row
                tmp2 = matrix[l][i]; # print("{} -> {}".format(tmp, matrix[l][i]))
                matrix[l][i] = tmp

            l += 1

        # print(matrix)
        return
