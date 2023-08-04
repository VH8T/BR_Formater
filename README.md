# Brewery Recipe Formatter Tool

This Brewery Recipe Formatter Tool is a user-friendly application developed by vh8t. Its purpose is to simplify the process of creating YAML format files for brew recipes used with the Minecraft plugin named Brewery. If you are not familiar with Brewery, you can find more information about it on their official page.
## How to Use the Tool

To use the Brewery Recipe Formatter Tool, follow the instructions below:

1. **Ensure Files are in the Same Directory:** Place the `main.py` and `icon.ico` files in the same directory on your computer. This is necessary for the tool to function correctly.

2. **No Additional Library Installation Required:** You do not need to install any additional libraries to run this tool. The `main.py` script will automatically check for and install any missing packages using the `subprocess` module.

3. **Run the Application:** Open a terminal or command prompt, navigate to the directory containing the files, and run the main.py script. This can typically be done by executing the following command:

    ```bash
   python main.py
   ```

4. **Enter Recipe Information:** The application will present you with a user interface where you can input the required information for your brew recipe.

5. **Wood Type Input Handling:** When specifying the wood type, you should enter the name of the wood type (e.g., "birch," "oak," "jungle," etc.) instead of a numerical value. The tool will handle the conversion from the wood type name to the corresponding numeric representation used in the YAML file.

6. **Available Wood Types:** The supported wood types for the brew recipe are: any, birch, oak, jungle, spruce, acacia, dark oak, crimson, warped, and mangrove.

7. **Handling Empty Values:** If any fields are left empty in the user interface, they will also be left empty in the generated YAML file. Alternatively, if specific fields are not required for your recipe, the tool will set those values to None in the YAML file.

8. **Mandatory Information:** Ensure that you provide values for the following fields, as they are required for a valid brew recipe:
   - Brew Name
   - Ingredients
   - Boiling Time

9. **Generate YAML File:** Once you have entered all the necessary information, click the "Submit" button in the user interface. The tool will create a YAML file named `<brew name>`.yml in the same directory as the `main.py` and `icon.ico` files. This file will contain your formatted brew recipe, ready for use with Brewery.

10. **Enjoy Brewing:** You can now use the generated YAML file with Brewery in Minecraft to create and enjoy your custom brew!

Please note that this tool is designed specifically for use with Brewery's YAML format for brew recipes. Ensure that you follow the required syntax and structure to create valid recipes for seamless integration with the plugin.

If you encounter any issues or have suggestions for improvement, feel free to reach out to **vh8t** on discord.

Happy brewing! 🍻