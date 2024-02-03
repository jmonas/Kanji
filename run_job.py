import subprocess

BATCH_SIZE = 4
N_GPUS = 2
ACCUMULATE_BATCHES = 1


command = [
    "python",
    "main.py",
    "-t",
    "--base",
    "kanji.yaml",
    "--gpus",
    "0,1,",
    "--scale_lr",
    "False",
    "--num_nodes",
    "1",
    "--check_val_every_n_epoch",
    "10",
    "--finetune_from",
    "/scratch/network/jmonas/.cache/huggingface/hub/models--CompVis--stable-diffusion-v-1-4-original/snapshots/f0bb45b49990512c454cf2c5670b0952ef2f9c71/sd-v1-4-full-ema.ckpt",
    "data.params.batch_size=4",
    "lightning.trainer.accumulate_grad_batches=1",
    "data.params.validation.params.n_gpus=2"
]
print("start")
# Execute the command
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

# Output the results
if process.returncode == 0:
    print('Command executed successfully')
    print(stdout.decode())
else:
    print('An error occurred')
    print(stderr.decode())