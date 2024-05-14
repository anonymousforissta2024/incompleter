#Source: https://stackoverflow.com/questions/71062211/filenotfounderror-despite-file-existing
def generate_dataset(agent_name: str, env_name: str, dataset_size: int, num_envs: int = 20, epsilon: float = 0.1,
                     network_root_folder: str = 'jax-models') -> Tuple[onp.ndarray, onp.ndarray, onp.ndarray,
                                                                       onp.ndarray, int]:

    num_actions = gym.make(f'{env_name}NoFrameskip-v0').action_space.n

    images_obs_dataset = onp.zeros((dataset_size, 84, 84, 4))
    ram_obs_dataset = onp.zeros((dataset_size, 128))
    q_values_dataset = onp.zeros((dataset_size, num_actions))
    action_dataset = onp.zeros(dataset_size)

    network_def, network_args = get_network_def(agent_name, num_actions)
    network_params = load_network_params(agent_name, env_name, network_root_folder=network_root_folder)

    return images_obs_dataset, ram_obs_dataset, q_values_dataset, action_dataset, episodes_run