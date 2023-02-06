import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.util.Scanner;

public class InputManager {
    public static void main(Path inputFilePath) {
        readFileWithSingleNewLine(inputFilePath);
    }

    public static void readFileWithSingleNewLine(Path filePath) {
        try {
            File aocInput = new File(String.valueOf(filePath));
            Scanner aocInputReader = new Scanner(aocInput);
            while (aocInputReader.hasNextLine()) {
                String input_data = aocInputReader.nextLine();
                System.out.println(input_data);
            }
            aocInputReader.close();
        }
        catch (FileNotFoundException e) {
            System.out.println("File is not found.");
            e.printStackTrace();
        }
    }

}