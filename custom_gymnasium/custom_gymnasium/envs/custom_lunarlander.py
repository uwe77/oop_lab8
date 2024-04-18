import numpy as np
import gymnasium as gym
from typing import TYPE_CHECKING, Optional
from custom_gymnasium.utils.init_lunar import INIT_LUNAR
from custom_gymnasium.utils.reset_lunar import RESET_LUNAR
from custom_gymnasium.utils.step_lunar import STEP_LUNAR


class CustomLunarLander_v1(INIT_LUNAR, RESET_LUNAR, STEP_LUNAR):
    def __init__(
        self,
        render_mode: Optional[str] = None,
        continuous: bool = False,
        gravity: float = -10.0,
        enable_wind: bool = False,
        wind_power: float = 15.0,
        turbulence_power: float = 1.5,):
        INIT_LUNAR.__init__(
            self=self,
            render_mode=render_mode,
            continuous=continuous,
            gravity=gravity,
            enable_wind=enable_wind,
            wind_power=wind_power,
            turbulence_power=turbulence_power,
        )

    def reset(
        self,
        *,
        seed: Optional[int] = None,
        options: Optional[dict] = None,):
        return RESET_LUNAR.reset(self=self, 
                                seed=seed,
                                options=options)
        
    def step(self, action):
        return STEP_LUNAR.step(self=self, action=action)
