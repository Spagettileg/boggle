import unittest
import boggle

class TestBoggle(unittest.TestCase):
    """
    Our Test Suite for Boggle Solver
    """
    
    def test_can_create_an_empty_grid(self):
        """
        Test to see if we can creae an empty grid
        """
        
        grid = boggle.make_grid(0,0) # Most basic of grids = 0 x 0
        self.assertEqual(len(grid),0) # Basic test for 0 x 0 grid. Test will fail due to 'make_grid' method not yet built
        
    def test_grid_size_is_width_times_height(self):
        """
        Test is to ensure that the total size of the grid
        is equal to width * height
        """
        
        grid = boggle.make_grid(2, 3)
        self.assertEqual(len(grid), 6) 
        
    def test_grid_coordinates(self):
        """
        Test to ensure that all of the coordinates
        inside the grid can be accessed
        """
        
        grid = boggle.make_grid(2, 2)
        self.assertIn((0, 0), grid) # Test to see if (0, 0) coordinates appear in a 2 x 2 grid
        self.assertIn((0, 1), grid) # Ditto for (0, 1) coordinates 
        self.assertIn((1, 0), grid) # Ditto for (1, 0) coordinates
        self.assertIn((1, 1), grid) # Ditto for (1, 1) coordinates
        self.assertNotIn((2, 2), grid) # Test to make sure (2, 2) coordinates dont appear in a 2 x 2 grid
         
         
         
         
        
    

   