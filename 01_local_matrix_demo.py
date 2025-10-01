# examples/01_local_matrix_demo.py
import asyncio
from aura import AuraLink

async def main():
    """
    This script demonstrates the core functionality of the Aura Singularity.
    It establishes a link and issues a simple directive, which will be
    decomposed by the Weaver and executed in parallel by the Local Matrix.
    """
    print("--- Aura Singularity: Local Matrix Demonstration ---")
    
    # Establish the link to your Singularity
    link = AuraLink()

    # Issue a directive. The command and parameters are illustrative.
    # The Weaver will decompose this into 16 tasks for the Local Matrix.
    results = await link.issue_directive(
        command="run_system_diagnostics",
        parameters={"depth": "full"}
    )
    
    print("\n--- Directive Execution Complete ---")
    print(f"Total tasks completed: {len(results)}")
    
    # Print the result of the first and last task as a sample
    if results:
        print(f"Sample result from first task: {results[0].result}")
        print(f"Sample result from last task: {results[-1].result}")

if __name__ == "__main__":
    # Note: This uses the top-level asyncio.run() available in Python 3.7+
    asyncio.run(main())
