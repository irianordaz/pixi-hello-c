import subprocess
import openmdao.api as om

class ExternalCComponent(om.ExplicitComponent):
    def setup(self):
#         self.add_input('x', val=1.0)
#         self.add_output('y', val=0.0)
        pass

    def compute(self, inputs, outputs):
        # Path to the binary built by Pixi
        executable = "./src/hello" 
        
        # Run the C binary as a subprocess
        # [Documentation for subprocess.run](https://docs.python.org)
        result = subprocess.run(
            [executable],
            # [executable, str(inputs['x'][0])],
            capture_output=False,
            text=True,
            check=True
        )
        
        # Parse the output from C's stdout
        # outputs['y'] = float(result.stdout.strip())

# --- Execution ---
prob = om.Problem()
prob.model.add_subsystem('c_code', ExternalCComponent())
prob.setup()

# prob.set_val('c_code.x', 21.0)
prob.run_model()

# print(f"Output from C binary: {prob.get_val('c_code.y')}")

