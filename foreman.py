import re

ASSET_RULES = {
	"action": {
		"prefix": "ATN",
		"example": "ATN_walkCycle_v003",
		"versioned": True
	},
	"armature": {
		"prefix": "ARM",
		"example": "ARM_characterRig_v003",
		"versioned": True
	},
	"environnement": {
		"prefix": "ENV",
		"example": "ENV_montagneModeling_v004",
		"versioned": True
	},
	"fx": {
		"prefix": "FX",
		"example": None
	},
	"image": {
		"prefix": "IMG",
		"example": "IMG_diffuseBrick2k.jpg"
	},
	"lattice": {
		"prefix": "LAT",
		"example": "LAT_facialDeform"
	},
	"library": {
		"prefix": "LIB",
		"example": "LIB_matLibShading"
	},
	"mesh": {
		"prefix": "MSH",
		"example": "MSH_buildingWalls"
	},
	"mask": {
		"prefix": "MSK",
		"example": "MSK_selectionHair"
	},
	"material": {
		"prefix": "MTL",
		"example": "MTL_leatherWorn"
	},
	"metarig": {
		"prefix": "MTA",
		"example": "MTA_bipedStandard"
	},
	"node_graph": {
		"prefix": "ND",
		"example": "NOD_renderSetup"
	},
	"palette": {
		"prefix": "PLT",
		"example": "PLT_characterColors"
	},
	"script": {
		"prefix": "SCT",
		"example": "SCT_autoBake_v001.py",
		"versioned": True
	},
	"simulation": {
		"prefix": "SIM",
		"example": None
	},
	"sound": {
		"prefix": "SND",
		"example": "SND_ambientForest_v001.wav",
		"versioned": True
	},
	"shape_key": {
		"prefix": "SPK",
		"example": "SPK_facialExpressions"
	},
	"text": {
		"prefix": "TXT",
		"example": "TXT_creditsFinal_v001",
		"versioned": True
	},
	"widget": {
		"prefix": "WGT",
		"example": "WGT_faceControl"
	},
	"world": {
		"prefix": "WLD",
		"example": "WLD_studioLighting_v002",
		"versioned": True
	}
}

class Foreman:
	def __init__(self, block_name: str, block_type: str, rules: dict = ASSET_RULES):
		self.block_name = block_name
		self.block_type = block_type
		self.rules = rules
		self.block_prefix = self.rules.get(block_type, {}).get("prefix", None)
		self.block_versioned = self.rules.get(block_type, {}).get("versioned", False)
		
		self.prefix, self.name, self.version = self.get_parts()

	def has_prefix(self):
		if not self.block_prefix:
			return None			

		return self.prefix == self.block_prefix.upper()
	
	def has_version(self):
		if not self.block_versioned:
			return None

		if not self.version:
			return False
		
		version_pattern = r"^v\d{3}$"
		return bool(re.match(version_pattern, self.version))

	def get_parts(self):
		parts = self.block_name.split("_")
		prefix = parts.pop(0) if self.block_prefix else None
		version = None if not self.block_versioned else parts.pop(-1)
		name = "_".join(parts)

		return prefix, name, version
	
	def is_case_valid(self):
		case_pattern = r"^[a-zA-Z]+([A-Z][a-z]+)+$"
		return bool(re.match(case_pattern, self.name))
