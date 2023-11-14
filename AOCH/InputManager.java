import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.nio.file.Path;
import java.util.List;

public class InputManagerTest {
    @Test
    public void testReadFile() {
        List<String> testFileInfo = InputManager.readFile(Path.of("tests/double_new_line_int_only.txt"));
        List<String> expectedOutput = List.of(
                "9686", "10178", "3375", "9638", "", "24919", "15983", "18045", "", "24872", "35761");
        Assertions.assertEquals(expectedOutput,testFileInfo);
    }

    @Test
    public void testGroupFileWithDoubleNewLine() {
        List<List<String>> testLineInfo = InputManager.groupFileWithDoubleNewLine(List.of(
                "9686", "10178", "3375", "9638", "", "24919", "15983", "18045", "", "24872", "35761"));
        List<List<String>> expectedOutput = List.of(
                List.of(new String[]{"9686", "10178", "3375", "9638"}),
                List.of(new String[]{"24919", "15983", "18045"}),
                List.of(new String[]{"24872", "35761"})
        );
        Assertions.assertEquals(expectedOutput,testLineInfo);
    }

    @Test
    public void testParseIntInLine() {
        List<Integer> testIntLinePositive = InputManager.parseIntInLine(
                " : 3249 weruhuiqwre723491'' \\ 3uh2h4 whiuh83279 32487692.34", false);
        List<Integer> expectedOutput = List.of(3249, 723491, 3, 2, 4, 83279, 32487692, 34);
        Assertions.assertEquals(expectedOutput, testIntLinePositive);
    }

    @Test
    public void testParseDirections() {
        List<InputManager.Coordinate> testParseInfo = InputManager.parseDirections(">>^v<<^<<>vv>");
        List<InputManager.Coordinate> expectedOutput = List.of(
                new InputManager.Coordinate(1, 0),
                new InputManager.Coordinate(1, 0),
                new InputManager.Coordinate(0, 1),
                new InputManager.Coordinate(0, -1),
                new InputManager.Coordinate(-1, 0),
                new InputManager.Coordinate(-1, 0),
                new InputManager.Coordinate(0, 1),
                new InputManager.Coordinate(-1, 0),
                new InputManager.Coordinate(-1, 0),
                new InputManager.Coordinate(1, 0),
                new InputManager.Coordinate(0, -1),
                new InputManager.Coordinate(0, -1),
                new InputManager.Coordinate(1, 0)

        );
        Assertions.assertEquals(expectedOutput, testParseInfo);
    }
}
