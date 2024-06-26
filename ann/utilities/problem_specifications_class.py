####################################################################################### 
# THIS SOURCE CODE IS PROPERTY OF THE GOVERNMENT OF THE UNITED STATES OF AMERICA. 
# BY USING, MODIFYING, OR DISSEMINATING THIS SOURCE CODE, YOU ACCEPT THE TERMS AND 
# CONDITIONS IN THE NRL OPEN LICENSE AGREEMENT. USE, MODIFICATION, AND DISSEMINATION 
# ARE PERMITTED ONLY IN ACCORDANCE WITH THE TERMS AND CONDITIONS OF THE NRL OPEN 
# LICENSE AGREEMENT. NO OTHER RIGHTS OR LICENSES ARE GRANTED. UNAUTHORIZED USE, SALE,
# CONVEYANCE, DISPOSITION, OR MODIFICATION OF THIS SOURCE CODE MAY RESULT IN CIVIL 
# PENALTIES AND/OR CRIMINAL PENALTIES UNDER 18 U.S.C. § 641. 
####################################################################################### 


#%% ------------------------------------------------------------ PROBLEM SPECIFICATIONS CLASS ------------------------------------------------------------

# This file implements a class for storing and managing problem specifications information.


#%% ------------------------------------------------------------ IMPORT LIBRARIES ------------------------------------------------------------

# Import standard libraries.


# Import custom libraries.
from save_load_utilities_class import save_load_utilities_class as save_load_utilities_class
from printing_utilities_class import printing_utilities_class as printing_utilities_class


#%% ------------------------------------------------------------ PROBLEM SPECIFICATIONS CLASS ------------------------------------------------------------

# Implement the problem specifications class.
class problem_specifications_class(  ):

    #%% ------------------------------------------------------------ CONSTRUCTOR ------------------------------------------------------------

    # Implement the class constructor.
    def __init__( self, num_inputs = None, num_outputs = None, temporal_domain = None, spatial_domain = None, domain_type = None, residual_function = None, residual_code = None, temporal_code = None, flow_functions = None, ibc_types = None, ibc_dimensions = None, ibc_condition_functions = None, ibc_placements = None, pde_name = '',  pde_type = '', save_path = None, load_path = None ):

        # Create an instance of the save-load utilities class.
        self.save_load_utilities = save_load_utilities_class(  )

        # Create an instance of the printing utilities class.
        self.printing_utilities = printing_utilities_class(  )

        # Store the number of inputs and outputs.
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs

        # Store the temporal and spatial domain.
        self.domain_type = domain_type
        self.temporal_domain = temporal_domain
        self.spatial_domain = spatial_domain

        # Store the residual function.
        self.residual_function = residual_function
        self.residual_code = residual_code
        self.temporal_code = temporal_code

        # Store the flow functions.
        self.flow_functions = flow_functions

        # Store the initial-boundary condition information.
        self.ibc_types = ibc_types
        self.ibc_dimensions = ibc_dimensions
        self.ibc_condition_functions = ibc_condition_functions
        self.ibc_placements = ibc_placements

        # Store the pde name and type.
        self.pde_name = pde_name
        self.pde_type = pde_type

        # Store the save and load paths.
        self.save_path = save_path
        self.load_path = load_path


    #%% ------------------------------------------------------------ PRINT FUNCTIONS ------------------------------------------------------------

    # Implement a function to print the hyperparameters.
    def print( self, num_dashes = 20, decoration_flag = True ):

        # Print a header.
        self.printing_utilities.print_header( 'PROBLEM SPECIFICATIONS SUMMARY', num_dashes, decoration_flag )

        # Print the number of inputs and outputs.
        print( 'Input / Output Information' )
        print( f'# of Inputs: {self.num_inputs}' )
        print( f'# of Outputs: {self.num_outputs}' )
        print( '\n' )

        # Print the temporal and spatial domain.
        print( 'Temporal / Spatial Domain' )
        print( f'Domain Type: {self.domain_type}' )
        print( f'Temporal Domain: {self.temporal_domain}' )
        print( f'Spatial Domain: {self.spatial_domain}' )
        print( '\n' )

        # Print the residual function.
        print( 'Residual Information' )
        print( f'Flow Function: {self.flow_functions}' )
        print( f'Residual Function: {self.residual_function}' )
        print( f'Residual Code: {self.residual_code}' )
        print( '\n' )

        # Print the initial-boundary condition information.
        print( 'Initial-Boundary Condition Information' )
        print( f'Initial-Boundary Condition Types: {self.ibc_types}' )
        print( f'Initial-Boundary Condition Dimensions: {self.ibc_dimensions}' )
        print( f'Initial-Boundary Condition Functions: {self.ibc_condition_functions}' )
        print( f'Initial-Boundary Condition Placements: {self.ibc_placements}' )
        print( '\n' )

        # Print the pde name and type.
        print( 'PDE Information' )
        print( f'PDE Name: {self.pde_name}' )
        print( f'PDE Type: {self.pde_type}' )
        print( '\n' )

        # Print the save and load paths.
        print( 'Save / Load Information' )
        print( f'Save Path: {self.save_path}' )
        print( f'Load Path: {self.load_path}' )

        # Print a footer.
        self.printing_utilities.print_footer( num_dashes, decoration_flag )


    #%% ------------------------------------------------------------ SAVE & LOAD FUNCTIONS ------------------------------------------------------------

    # Implement a function to save the problem specifications.
    def save( self, save_path = None, file_name = r'problem_specifications.pkl' ):

        # Determine whether to use the stored save path.
        if save_path is None:                               # If the save path was not provided...

            # Use the stored save path.
            save_path = self.save_path

        # Save the problem specifications.
        self.save_load_utilities.save( self, save_path, file_name )


    # Implement a function to load problem specifications.
    def load( self, load_path = None, file_name = r'problem_specifications.pkl' ):

        # Determine whether to use the stored load path.
        if load_path is None:                               # If the load path was not provided...

            # Use the stored load path.
            load_path = self.load_path

        # Load the problem specifications.
        self = self.save_load_utilities.load( load_path, file_name )

        # Return the problem specifications.
        return self

