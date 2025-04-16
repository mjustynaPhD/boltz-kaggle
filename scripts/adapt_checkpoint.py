from dataclasses import asdict

import hydra
import omegaconf
import torch
from train.train import TrainConfig, DataConfig

from boltz.main import BoltzDiffusionParams
from boltz.model.model import Boltz1

checkpoint_path = "../.boltz-model/boltz1_conf.ckpt"
print(f"Loading checkpoint from {checkpoint_path}")
checkpoint = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
# Remove the "PairformerModule." prefix from the keys in the state_dict
print("Removing 'PairformerModule.' prefix from state_dict keys")
new_state_dict = {}
for key, value in checkpoint["state_dict"].items():
    if not key.startswith("pairformer_module.") and \
       not key.startswith("msa_module.") :
    #    not key.startswith("confidence_module."):
        print(key)
        new_state_dict[key] = value

# Save the modified state_dict to a new file
print("Saving modified checkpoint")
new_checkpoint_path = "../.boltz-model/boltz1_no_PairFormer.ckpt"
torch.save(new_state_dict, new_checkpoint_path)
print(f"Checkpoint saved to {new_checkpoint_path}")

recycling_steps: int = 3
sampling_steps: int = 200
diffusion_samples: int = 1
write_full_pae: bool = False
write_full_pde: bool = False

predict_args = {
    "recycling_steps": recycling_steps,
    "sampling_steps": sampling_steps,
    "diffusion_samples": diffusion_samples,
    "write_confidence_summary": True,
    "write_full_pae": write_full_pae,
    "write_full_pde": write_full_pde,
}
print("Loading model")
# diffusion_params = BoltzDiffusionParams()

raw_config = "train/configs/structure.yaml"
raw_config = omegaconf.OmegaConf.load(raw_config)


# Instantiate the task
cfg = hydra.utils.instantiate(raw_config)
cfg = TrainConfig(**cfg)

# config_dict = cfg.model

# model_module: Boltz1 = Boltz1.load_from_checkpoint(
#         checkpoint,
#         strict=True,
#         predict_args=predict_args,
#         map_location="cpu",
#         diffusion_process_args=asdict(diffusion_params),
#         ema=False,
#     )


model_module: Boltz1 = cfg.model
print("My keys")
print(model_module.state_dict().keys())
print("Loading model from checkpoint")

model_module.load_state_dict(
                    state_dict=torch.load(new_checkpoint_path, map_location="cpu", weights_only=False),
                    strict=True,
                    )
model_module.eval()
print("Successfully loaded model")
