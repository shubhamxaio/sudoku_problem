class Solution:
	# checking if count of element in a list is less than 1
	def check_sudoku_list(self, sudoku_list):
		for element in sudoku_list:
			if element != '.' and sudoku_list.count(element) > 1:
				return False
		return True

	
	def check_three_cross_matrix(self, start_val, end_val, diff_val, limit_val, sudoku_list):
		for index_ in range(start_val, end_val, diff_val):
			s_list = []
			while index_ < limit_val:
				s_list.extend([sudoku_list[index_], sudoku_list[index_+1], sudoku_list[index_+2]])
				index_ +=9
			valid = self.check_sudoku_list(s_list)
			if not valid:
				return False
			limit_val += 3
		return True


	def check_matrix(self, sudoku_list):
		valid = False
		first_valid = self.check_three_cross_matrix(start_val=0, end_val=9, diff_val=3, limit_val=21, sudoku_list=sudoku_list)
		if first_valid:
			second_valid = self.check_three_cross_matrix(start_val=27, end_val=36, diff_val=3, limit_val=47, sudoku_list=sudoku_list)
			if second_valid:
				third_valid = self.check_three_cross_matrix(start_val=54, end_val=63, diff_val=3, limit_val=74, sudoku_list=sudoku_list)
				if third_valid:
					valid = True
		return valid


	def check_row(self, sudoku_list):
		for row in range(0, len(sudoku_list)-8, 9):
			sliced_list = sudoku_list[row:row+9]
			valid = self.check_sudoku_list(sliced_list)
			if not valid:
				return False
		return True

	def check_column(self, sudoku_list):
		for row in range(0,8):
			s_list = []
			for col in range(9):
				s_list.append(sudoku_list[row])
				row+=9
			valid = self.check_sudoku_list(s_list)
			if not valid:
				return False
		return True

	# checking validation of sudoku using three functions
	def is_valid_sudoku(self, sudoku_list):
		is_block_valid = self.check_matrix(sudoku_list) # checking for 3*3 matrix
		is_row_valid = self.check_row(sudoku_list) # checking for row
		is_cloumn_valid = self.check_column(sudoku_list) # checking for column

		if is_block_valid and is_row_valid and is_cloumn_valid:
			return 1
		else:
			return 0

	# creating sudoku in a list
	def create_sudoku_list(self, input_list):
		arr = []
		for item in input_list:
			for i in item:
				try:
					arr.append(int(i))
				except:
					arr.append(i)
		return arr

if __name__ == '__main__':
	# input_list = input().split(' ')
	# e.g.
	# input_list = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
	input_list = "....5..1. .4.3..... .....3..1 8......2. ..2.7.... .15...... .....2..." ".2.9..... ..4......"
	input_list = input_list.split(' ')
	solution = Solution()
	sudoku_list = solution.create_sudoku_list(input_list)
	result = solution.is_valid_sudoku(sudoku_list)
	if result:
		print("Sudoku is VALID")
	else:
		print("Sudoku is INVALID")
