from datasets import load_dataset, DatasetDict

dataset = load_dataset("faridlab/deepspeak_v1", trust_remote_code=True)

if isinstance(dataset, DatasetDict):
	dataset.save_to_disk("export")
else:
	dataset = DatasetDict({"train": dataset})
	dataset.save_to_disk("export")