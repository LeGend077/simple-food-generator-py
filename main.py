from argparse import BooleanOptionalAction
import json
import string
from xmlrpc.client import Boolean, boolean
IDENTIFIER_PREF = input("\nPlease enter your item identifier prefix: ")
IDENTIFIER = input("\nPlease enter your food identifier name: ")
USE_DURATION = int(input("\nUse Duration: "))
NUTRITION = int(input("\nNutrition Value: "))
SATURATION_MODIFIER = input("\nSaturation Modifier Value (Accepts- poor, low, normal, good, supernatural): ")
file = {
  "format_version": "1.10",
  "minecraft:item": {
    "description": {
      "identifier": IDENTIFIER_PREF + ':' + IDENTIFIER
    },

    "components": {
      "minecraft:use_duration": USE_DURATION,
      "minecraft:food": {
        "nutrition": NUTRITION,
        "saturation_modifier": SATURATION_MODIFIER,
        "can_always_eat": str(input("\nCan always eat (true or false): "))
      }
    }
  }
}
json_object = json.dumps(file, indent = 4)
with open(IDENTIFIER+".json", "w") as outfile:
	outfile.write(json_object)