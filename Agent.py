# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.
# Allowable libraries are Python 3.8, Pillow 8.1.0, numpy 1.19.1, and OpenCV4.2.0
# OpenCV 4.2.0, opencv-contrib-python-headless. Non-headless versions of OpenCV will work,
# but the contrib modules of OpenCV like imshow() will not work.
    
from PIL import Image
import numpy as np
#import cv2

class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an int representing its
    # answer to the question: 1, 2, 3, 4, 5, or 6. Strings of these ints 
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName(). Return a negative number to skip a problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    # Remember to return the answer [Key], not the name, as the ANSWERS ARE SHUFFLED.
    # Use var = problem.figures["A"].visualFilename to open files
    # Do not use Absolute pathing to open files
    def Solve(self, problem):
        # Load images A, B, and C
        im_a = Image.open(problem.figures["A"].visualFilename).convert("1")
        im_b = Image.open(problem.figures["B"].visualFilename).convert("1")
        im_c = Image.open(problem.figures["C"].visualFilename).convert("1")

        # Calculate horizontal and vertical shifts between A and B
        shift_x = self.calculate_horizontal_shift(im_a, im_b)
        shift_y = self.calculate_vertical_shift(im_a, im_b)

        # Load images 1, 2, 3, 4, 5, and 6
        options = []
        for i in range(1, 7):
            option = Image.open(problem.figures[str(i)].visualFilename).convert("1")
            options.append(option)

        # Compare shifts between C and other options
        matching_options = []
        for option in options:
            option_shift_x = self.calculate_horizontal_shift(im_c, option)
            option_shift_y = self.calculate_vertical_shift(im_c, option)
            if shift_x == option_shift_x and shift_y == option_shift_y:
                matching_options.append(option)

        if matching_options:
            for option_name, option_figure in problem.figures.items():
                if option_figure.visualFilename == matching_options[0].filename:
                    option_number = int(option_name)
                    return option_number

        return -1  # Return -1 if no matching image is found

    def calculate_horizontal_shift(self, image1, image2):
        width1, _ = image1.size
        width2, _ = image2.size
        return width2 - width1

    def calculate_vertical_shift(self, image1, image2):
        _, height1 = image1.size
        _, height2 = image2.size
        return height2 - height1

def main():
    agent = Agent()
    problem = None  # Replace with the problem you want to solve
    answer = agent.Solve(problem)
    print("Answer:", answer)

if __name__ == "__main__":
    main()



    """def Solve(self, problem):
        def calculate_answer ():
            black_pixels_a = self.count_black_pixels(im_a)
            black_pixels_b = self.count_black_pixels(im_b)
            black_pixels_c = self.count_black_pixels(im_c)

        # Calculate difference in black pixels between A and B
            diff_a_b = black_pixels_a - black_pixels_b

        # Check differences with C images
            closest_match_index = -1
            closest_match_diff = float('inf')  # Initialize with a large value

            for i, image_path in enumerate(image_opt):
                im = Image.open(image_path)
                black_pixels_c = self.count_black_pixels(im)
                diff_c = black_pixels_c - black_pixels_a

            if diff_c == diff_a_b:
                return i + 1  # Return the index of the exact matching image

            # Check if the difference is closer to the desired difference
            if abs(diff_c - diff_a_b) < closest_match_diff:
                closest_match_diff = abs(diff_c - diff_a_b)           
                closest_match_index = i + 1
            return closest_match_index  
        # Load images
        image_opt = [
            problem.figures["1"].visualFilename,
            problem.figures["2"].visualFilename,
            problem.figures["3"].visualFilename,
            problem.figures["4"].visualFilename,
            problem.figures["5"].visualFilename,
            problem.figures["6"].visualFilename,
            
        ]

        if problem.problemType == "3x3":
            image_opt.append(problem.figures["7"].visualFilename)
            answer = calculate_answer(problem)
            results = open("results.txt", "w")
            results.write("%s,%s,%d" % (set.name, problem.name, answer))
            results.close()
            image_opt.append(problem.figures["8"].visualFilename)
            im_d = Image.open(problem.figures["D"].visualFilename)
            im_e = Image.open(problem.figures["E"].visualFilename)
            im_f = Image.open(problem.figures["F"].visualFilename)
            im_g = Image.open(problem.figures["G"].visualFilename)
            im_h = Image.open(problem.figures["H"].visualFilename)

        im_a = Image.open(problem.figures["A"].visualFilename)
        im_b = Image.open(problem.figures["B"].visualFilename)
        im_c = Image.open(problem.figures["C"].visualFilename)
        shift_x = self.calculate_horizontal_shift(im_a, im_b)
        shift_y = self.calculate_vertical_shift(im_a, im_b)
        print(image_opt)
        matching_options = image_opt

        for i in range(1, 7):
            im_option = Image.open(problem.figures[str(i)].visualFilename)
            option_shift_x = self.calculate_horizontal_shift(im_c, im_option)
            option_shift_y = self.calculate_vertical_shift(im_c, im_option)

            if shift_x == option_shift_x and shift_y == option_shift_y:
                matching_options.append(i)

        if matching_options:
            return matching_options[0]

        # Process of elimination
        remaining_options = self.eliminate_high_shifts(im_c, matching_options)
        return min(remaining_options)

    def calculate_horizontal_shift(self, image1, image2):
        width1, _ = image1.size
        width2, _ = image2.size
        return width2 - width1

    def calculate_vertical_shift(self, image1, image2):
        _, height1 = image1.size
        _, height2 = image2.size
        return height2 - height1

    def eliminate_high_shifts(self, image, options):
        remaining_options = []
        for option in options:
            im_option = Image.open(problem.figures[str(option)].visualFilename)
            option_shift_x = self.calculate_horizontal_shift(image, im_option)
            option_shift_y = self.calculate_vertical_shift(image, im_option)

            if abs(option_shift_x) <= 10 and abs(option_shift_y) <= 10:
                remaining_options.append(option)
        print(remaining_options)
        return remaining_options
    
    def count_black_pixels(self, image):
            # Convert the image to grayscale if needed  
            if image.mode != 'L':
                image = image.convert('L')

            # Get the image data as a list of pixel values
            pixels = list(image.getdata())

            # Count the number of black pixels (assuming black is represented by 0)
            black_pixels = sum(pixel == 0 for pixel in pixels)

            return black_pixels"""
    # Calculate number of black pixels in A, B and C
    # Return the index of the closest matching image
    """def _shimmer(sample_binary_img):

        tolerance = ""10
        shimmer =[]

        for x_roll in range(-tolerance, tolerance + 1 ):
            for y_roll in range (-tolerance, tolerance + 1):
                shimmer.append(np.roll(np.roll(sample_binary_img, x_roll, 0), y_roll ,1))

        return shimmer

    def best_shim_bin(target, test_binary_array):

        test_shims = ImageProcessor.adv_shimmer(test_binary_array)
        og_img_diff = np.shape(target)[0] * np.shape(target)[1]
        for shim_img in test_shims:
            diff_img = abs(shim_img - target)
            shim_diff = np.sum(diff_img)
        return shim_diff"""