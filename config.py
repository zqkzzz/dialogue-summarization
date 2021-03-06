class Config:
    pretrained_model_name_or_path = 'bert-base-chinese'

    local = True
    # model params
    num_train_epochs = 1
    dim_model = 768
    num_heads = 8
    dim_ff = 3072
    dropout = 0.5
    num_layers = 3
    max_src_num_length = 128
    max_utter_num_length = 128
    max_decode_output_length = 256
    utter_type = 3
    vocab_size = 21128
    max_grad_norm = 1.0
    is_coverage = True
    pointer_gen = True
    # train
    #   dropout0.3 cover-weight 2
    seed = 4027
    device = 'cpu' if local else 'cuda'
    use_pickle = True
    data_dir = './data-dev' if local else './data'
    train_data_path = f'{data_dir}/AutoMaster_TrainSet.csv'
    predict_data_path = f'{data_dir}/AutoMaster_TestSet.csv'
    predict_output = 'prediction_result'
    learning_rate = 4e-3
    fn = 'ckpt'
    load = False
    pickle_path = f'{data_dir}/train_data.pkl'
    predict_pickle_path = f'{data_dir}/predict_data.pkl'
    betas = (0.9, 0.99)
    gradient_accumulation_steps = 8
    weight_decay = 0.0001
    adam_epsilon = 1e-8
    warmup_steps = 1000
    local_rank = -1
    batch_size = 1
    beam_size = 5
    cov_loss_wt = 2.0
    eps = 1e-12
    logger_path = f'{data_dir}/all.log'
