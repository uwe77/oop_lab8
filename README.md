# LAB8

## Clone this repo
```
cd ~/
git clone https://github.com/uwe77/oop_lab8.git
```
## LAB
### Class Diagram

```mermaid
graph RL
    subgraph Function
        __init__
        reset
        step
    end
    id1[LunarLander]
    id2[Base_Lander]
    id3[CustomLunarLander_v1]
    id2-.-Function
    id3--inherit-->id2--inherit-->id1
```
### Task:
Add a fuel system into Custom Lander.
Add an input parameter to specify the total fuel when initializing Custom Lander.
Ensure that the lander's fuel decreases when its action is not zero.
Reset the fuel when Custom Lander is reset.
Modify the code at:
oop_lab8/custom_gymnasium/custom_gymnasium/envs/custom_lunarlander.py

### Hint:
You'll need to use super() to call the parent class's constructor{init(), reset(), step()}.
Then you can integrate the fuel system into Custom Lander.
Please ensure that you specify the input and output requirements of each function.

### You can refer to the code from the file location below
oop_lab8/custom_gymnasium/custom_gymnasium/envs/box2d/lunar_lander.py
oop_lab8/custom_gymnasium/custom_gymnasium/envs/utils/base_lander.py
oop_lab8/custom_gymnasium/custom_gymnasium/envs/custom_lunarlander.py

## How To Run
First, enter the Docker and set up the environment by following the commands below.
```
cd ~/oop_lab8
source Docker/docker_run.sh
source environment.sh
```
If you've completed the missing code, you can run the custom lander by following the commands below.
(Ensure that your terminal is inside the Docker environment where the setup has been completed.)
```
cd ~/oop_lab8/scripts
python3 play_lunarlander.py
```
Or you can just follow the gif...
<img src="./images/howtolaunch.gif"/>

## How should it looks like
<img src="./images/customlander.gif"/>

## How to play
Use the 'w', 'a', 'd' keys to control the main, right, and left engines, respectively, and try to land in the area between the two flags before running out of fuel.