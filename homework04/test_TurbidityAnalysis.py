import pytest
from turbidityAnalysis import calculateTurbidity, calculateTimetoSafeTurbidity

def testCalculateTurbidity():
    """Test the calculateTurbidity function with different inputs"""

    # Basic(edit) calculations
    assert calculateTurbidity([1.0], [1.0]) == 1.0
    assert calculateTurbidity([2.0], [0.5]) == 1.0
    assert calculateTurbidity([1.0, 2.0], [1.0, 0.5]) == 1.0

    # Edge cases
    assert calculateTurbidity([0.0], [1.0]) == 0.0
    assert calculateTurbidity([1.0], [0.0]) == 0.0

    # Type check
    assert isinstance(calculateTurbidity([1.0, 2.0], [1.0, 0.5]), float)

def testCalculateTimetoSafeTurbidity():
    """Test the calculateTimetoSafeTurbidity function with different inputs."""

    # Below or at threshold
    assert calculateTimetoSafeTurbidity(0.9) == 0.0
    assert calculateTimetoSafeTurbidity(1.0) == 0.0

    # Simple decay tests 
    assert calculateTimetoSafeTurbidity(1.02) > 0.0
    assert calculateTimetoSafeTurbidity(2.0) > 0.0

    # Type check
    assert isinstance(calculateTimetoSafeTurbidity(1.5), float)

    # Large turbidity values
    assert calculateTimetoSafeTurbidity(10.0) > calculateTimetoSafeTurbidity(2.0)


if __name__ == "__main__":
    pytest.main()
    pytest.main()
    pytest.main()
    pytest.main()
    pytest.main()