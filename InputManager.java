import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;

public class InputManager {

    public static List<String> readFileWithSingleNewLine(Path filePath) {
        try {
            return Files.readAllLines(filePath);

        } catch (IOException e) {
            e.printStackTrace();
            throw new RuntimeException(e);
        }

    }


    public static List<List<String>> readFileWithDoubleNewLine(Path filePath) {
        try {
            List<String> input_lines = Files.readAllLines(filePath);
            List<List<String>> grouped_input_lines = new ArrayList<>();
            List<String> group = new ArrayList<>();
            for (String input_line : input_lines) {
                if (input_line.equals("")) {
                    grouped_input_lines.add(group);
                    group = new ArrayList<>();
                } else {
                    group.add(input_line);
                }
            }
            return grouped_input_lines;

        } catch (IOException e) {
            e.printStackTrace();
            throw new RuntimeException(e);
        }
    }
}