import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.List;

public class InputManager {
    public static List<String> readFile(Path filePath) {
        try {
            return Files.readAllLines(filePath);

        } catch (IOException e) {
            e.printStackTrace();
            throw new RuntimeException(e);
        }
    }

    public static List<List<String>> readFile(Path filePath, boolean doubleNewLine) {
        if (doubleNewLine) {
            try {
                return Arrays.stream(Files.readString(filePath).split("\n\n"))
                        .map(x -> Arrays.stream(x.split("\n")).toList()).toList();

            } catch (IOException e) {
                e.printStackTrace();
                throw new RuntimeException(e);
            }
        }
        else {
            return null;
        }
    }
}