# ImagesetGenerator
A image-data-set generator for artificial intelligence training purpose.

How it works: Basicly it walk through a root folder and get all the sub folder as a class name
                then it create a corresponding folder with the same class name to save csv files
                using pillow to read imagefiles and transform into rgb data saved in numpy matrix
                then save the matrix as a csv file, when loading a csv it tranlate the matrix back
                with some dataset generator functions, it can devide the whole set into train set,
                validate set and test set.And it can create batches of train set for SGD or other
                training method.

What to do: First, you have to do some basic configuration
                1. set the directory
                        Using: .set_image_root_dir()
                               .set_csv_root_dir()
                2. set the booleans
                        Using: .set_show_image()
                               .set_reshape_image()
                3. set the standard shape
                        Using: .set_image_std()

            Next, you can call the generate function to start building
                        Using: .generate()

            Finally, when using the imageset, call the function(Unfinished)
