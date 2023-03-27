import subprocess
import traci
import traci.constants as tc

def run():
    # Start SUMO with the given configuration file
    sumo_binary = "sumo-gui"  # Or "sumo" for headless mode
    config_file = "data/whitefield.sumocfg"
    sumo_cmd = [sumo_binary, "-c", config_file]
    traci.start(sumo_cmd)
    step = 0

    while True:
        traci.simulationStep()

        # TODO: Implement adaptive traffic control logic here

        step += 1

    # Close TraCI and stop the SUMO simulation
    traci.close()
    sumo_proc.terminate()

if __name__ == "__main__":
    run()
