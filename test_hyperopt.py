import chemprop

arguments = [
    '--data_path', 'data/ecoil_hyperopt.csv',
    '--dataset_type', 'classification',
    '--num_iters', '20',
    '--features_generator', 'rdkit_2d_normalized', '--no_features_scaling',
    '--config_save_path', 'config_benchmark_opt.json',
    '--hyperopt_checkpoint_dir', 'hypOpt_opt',
    '--save_smiles_splits',
    '--log_dir', 'hyperopt_opt_log',
    '--depth', '5',
    '--hidden_size', '1600',
    '--ffn_num_layers', '1',
    '--dropout', '0.35',
    '--search_parameter_keywords', 'depth', 'hidden_size', 'ffn_num_layers', 'dropout'
]

args = chemprop.args.HyperoptArgs().parse_args(arguments)
hyper = chemprop.hyperparameter_optimization.hyperopt(args)