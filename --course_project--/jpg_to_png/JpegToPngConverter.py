import os
import sys
from PIL import Image


if __name__ == "__main__":
    try:
        convert_command = sys.argv[1]

        if convert_command == "-h" or convert_command == "--help":
            message = r"""
                        --- Welcome ---
                        
                        Hi, im Alireza Fazeli and i made this application with love.
                        this application is very simple and i made this application to make easy your life.
                        so pleas follow my linkedin and github :
                        https://linkedin.com/in/alirezafazeli
                        https://github.com/alirezafazeli8
                        
                        What you need ?
                        
                        first of all you need two path. first is your JPEG file path.
                        
                        for example : "D:\\3- photo\yakuza.jpg"
                        
                        and second is your destination path. 
                        for example : "C:\Users\Alireza\Desktop"
                        
                        just this :). follow me and learn the commands.
                        
                        -c , --convert :
                            with one of these commands you can convert your JPEG file to PNG.
                            for example : python JpegToPngConverter.py -c "D:\\3- photo\yakuza.jpg" "C:\Users\Alireza\Desktop"
                            
                        -h , --help : 
                            now you are in fucking help :))))
                            
                        -v : 
                            you can see where we are. maybe later i or with your help , i develop more this app.
                            
                            
                        bye bye :)))) 

                        
                        ---------------            
                    """

            print(message)
        elif convert_command == "-c" or convert_command == "--convert":

            # get data user from terminal
            file_path, save_file_path = sys.argv[2], sys.argv[3]

            # open user Image
            user_image = Image.open(file_path)

            # find main file name
            file_name = os.path.basename(file_path)[:-4:]

            # save image as png
            png_file_path = f"{save_file_path}\\{file_name}.png"
            user_image.save(png_file_path, "png")

            # done message
            print(
                f"""
                    -- DONE ---
                    Your File Saved In {png_file_path}
                    -----------
                    """
            )

        elif convert_command == "-v" or convert_command == "--version":
            pass
        else:
            print(
                """
                        --- Error ---
                        use -h or --help 
                        -------------
                    """
            )
    except IndexError:
        print(
            """
                   ---Invalid Command---
                   use -h or --help
                   ---------------------
                  """
        )
    except FileNotFoundError:
        print(
            """
            -- Error --
            i can't find the file
            pleas insert correct file path
            use -h or --help to know how to work
            -----------
            
            """
        )
