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
    '--data_path', '../antibiotics/ecoli_scaffold/train_val.csv',
    '--dataset_type', 'classification',
    '--save_dir', '../checkpoints/ecoli_20iter_feat_110_001_U/train_20folds_1ensem_class',
    '--epochs', '30',
    '--save_smiles_splits',
    '--config_path', '../checkpoints/ecoli_20iter_feat_110_001_U/hyopt_1ensem_no_class/config_U.json',
    '--features_generator', 'rdkit_2d_normalized', '--no_features_scaling',
    '--num_folds', '20',
    '--save_preds',
    '--separate_test_path', '../antibiotics/test_ecoli_antibiotics.csv'
]

args = chemprop.args.TrainArgs().parse_args(arguments)
mean_score, std_score = chemprop.train.cross_validate(args=args, train_func=chemprop.train.run_training)