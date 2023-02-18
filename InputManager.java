import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class InputManagerTest {
    @Test
    public void testReadFile() {
        List<String> testFileInfo = InputManager.readFile(Path.of("tests/double_new_line_int_only.txt"));
        String[] expectedOutputTemp = {"9686", "10178", "3375", "9638", "", "24919", "15983", "18045", "", "24872", "35761"};
        List<String> expectedOutput = Arrays.asList(expectedOutputTemp);
        Assertions.assertEquals(expectedOutput,testFileInfo);
    }

    @Test
    public void testGroupFileWithDoubleNewLine() {
        String[] testLineInfoTemp = {"9686", "10178", "3375", "9638", "", "24919", "15983", "18045", "", "24872", "35761"};
        List<List<String>> testLineInfo = InputManager.groupFileWithDoubleNewLine(Arrays.asList(testLineInfoTemp));
        String[][] expectedOutputTemp = {{"9686", "10178", "3375", "9638"}, {"24919", "15983", "18045"}, {"24872", "35761"}};
        List<List<String>> expectedOutput = Arrays.stream(expectedOutputTemp).map(Arrays::asList).toList();
        Assertions.assertEquals(expectedOutput,testLineInfo);
    }

    @Test
    public void testParseIntInLine() {
        List<Integer> testIntLinePositive = InputManager.parseIntInLine(" : 3249 weruhuiqwre723491'' \\ 3uh2h4 whiuh83279 32487692.34", false);
        int[] expectedOutputTemp = {3249, 723491, 3, 2, 4, 83279, 32487692, 34};
        List<Integer> expectedOutput = Arrays.stream(expectedOutputTemp).boxed().toList();
        Assertions.assertEquals(expectedOutput, testIntLinePositive);
    }

    @Test
    public void testParseDirections() {
        List<InputManager.Coordinate> testParseInfo = InputManager.parseDirections(">>^v<<^<<>vv>");
        List<InputManager.Coordinate> expectedOutput = List.of(
                new InputManager.Coordinate(1, 0),
                new InputManager.Coordinate(1, 0),
                new InputManager.Coordinate(1, 0),
                new InputManager.Coordinate(1, 0),
                new InputManager.Coordinate(1, 0),
                new InputManager.Coordinate(1, 0),
                new InputManager.Coordinate(1, 0)
        );
        Assertions.assertEquals(expectedOutput, testParseInfo);
    }
}
