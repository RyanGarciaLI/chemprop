import chemprop


# arguments = [
#     # '--data_path', 'tests/data/classification.csv',
#     '--data_path', 'data/ecoil.csv',
#     '--dataset_type', 'classification',
#     '--save_dir', 'test_checkpoints_class',
#     '--epochs', '30',
#     '--save_smiles_splits',
#     '--depth', '10',
#     '--hidden_size', '300',
#     '--dropout', '0.35',
#     '--ffn_num_layers', '3'
# ]
arguments = [
    '--data_path', 'data/ecoil.csv',
    '--dataset_type', 'classification',
    '--save_dir', 'ecoil_111_000_1',
    '--epochs', '30',
    '--save_smiles_splits',
    '--config_path', 'config_benchmark_opt.json',
    '--features_generator', 'rdkit_2d_normalized', '--no_features_scaling',
    '--num_folds', '20',
    '--save_preds',
    '--quiet',
]

args = chemprop.args.TrainArgs().parse_args(arguments)
mean_score, std_score = chemprop.train.cross_validate(args=args, train_func=chemprop.train.run_training)