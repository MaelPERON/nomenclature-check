ASSET_RULES = {
    "action": {
        "prefix": "ATN",
        "example": "ATN_walk_cycle_v003",
        "versioned": True
    },
    "armature": {
        "prefix": "ARM",
        "example": "ARM_character_rig_v003",
        "versioned": True
    },
    "environnement": {
        "prefix": "ENV",
        "example": "ENV_montagne_modeling_v004",
        "versioned": True
    },
    "fx": {
        "prefix": "FX",
        "example": None
    },
    "image": {
        "prefix": "IMG",
        "example": "IMG_diffuse_brick_2k.jpg"
    },
    "lattice": {
        "prefix": "LAT",
        "example": "LAT_facialDeform"
    },
    "library": {
        "prefix": "LIB",
        "example": "LIB_matLib_shading"
    },
    "mesh": {
        "prefix": "MSH",
        "example": "MSH_building_walls"
    },
    "mask": {
        "prefix": "MSK",
        "example": "MSK_selection_hair"
    },
    "material": {
        "prefix": "MTL",
        "example": "MTL_leather_worn"
    },
    "metarig": {
        "prefix": "MTA",
        "example": "MTA_biped_standard"
    },
    "node_graph": {
        "prefix": "ND",
        "example": "NOD_renderSetup"
    },
    "palette": {
        "prefix": "PLT",
        "example": "PLT_character_colors"
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
        "example": "SND_ambient_forest_v001.wav",
        "versioned": True
    },
    "shape_key": {
        "prefix": "SPK",
        "example": "SPK_facial_expressions"
    },
    "text": {
        "prefix": "TXT",
        "example": "TXT_credits_final_v001",
        "versioned": True
    },
    "widget": {
        "prefix": "WGT",
        "example": "WGT_faceControl"
    },
    "world": {
        "prefix": "WLD",
        "example": "WLD_studio_lighting_v002",
        "versioned": True
    }
}

class Foreman:
	def __init__(self, block_name: str, block_type: str):
		self.block_name = block_name
		self.block_type = block_type
		self.block_prefix = ASSET_RULES.get(block_type, {}).get("prefix", None)
		self.block_versioned = ASSET_RULES.get(block_type, {}).get("versioned", False)
		
		self.prefix, self.name, self.version = self.get_parts()
