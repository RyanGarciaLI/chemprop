python hyperparameter_optimization.py \
    --data_path ../antibiotics/ecoli_scaffold/train_val.csv \
    --dataset_type classification \
    --num_iters 20 \
    --features_generator rdkit_2d_normalized --no_features_scaling \
    --config_save_path ../checkpoints/ecoli_20iter_feat_110_001_U_3D/hyopt_1ensem_no_class_2/config_U_3D.json \
    --hyperopt_checkpoint_dir ../checkpoints/ecoli_20iter_feat_110_001_U_3D/hyopt_1ensem_no_class_2 \
    --log_dir ../checkpoints/ecoli_20iter_feat_110_001_U/hyopt_1ensem_no_class_2 > output.txt