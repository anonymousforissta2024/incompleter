#Source: https://stackoverflow.com/questions/65454097/exception-has-occurred-attributeerror-list-object-has-no-attribute-get-wh
STOCK_DIM = 422 # INITIAL_BALANCE, Amount_of_shares,  60 days * (Norm_close, 1m/2m/3m/1y ret, macd,rsi) 
INITIAL_ACCOUNT_BALANCE = 1000000
TRANSACTION_FEE_PERCENT = 0.01
REWARD_SCALING = 1e-5
HMAX_NORMALIZE = 100
N = config.PREV_DATA_POINTS


class StockEnv_Train(gym.Env):
    def __init__(self,df,day = 374):
        # day set to 260 since we need to account for the annual returns that only start around 252 days,
        # macd only starts from 254
        # we add 63 days to this to account for the historical data
        self.day = day
        self.df = df
        self.action_space = spaces.Box(low = -1,high = 1,shape =(1,) )
        self.observation_space = spaces.Box(low = 0, high = np.inf, shape = (STOCK_DIM,))
        self.terminal = False

        self.state = [INITIAL_ACCOUNT_BALANCE] + [0] + self.df.iloc[self.day-N:self.day,1].tolist() + \
                        self.df.iloc[self.day-N:self.day,2].tolist() + self.df.iloc[self.day-N:self.day,3].tolist() + \
                        self.df.iloc[self.day-N:self.day,4].tolist() + self.df.iloc[self.day-N:self.day,5].tolist() + \
                        self.df.iloc[self.day-N:self.day,6].tolist() + self.df.iloc[self.day-N:self.day,7].tolist()

        self.reward = 0
        self.asset_memory = [INITIAL_ACCOUNT_BALANCE]
        self.cost = 0
        self.rewards_memory = []
        self.trades = 0

        self._seed()

    
    def _sell_stock(self,action):
        if self.state[1] > 0:
            self.state[0] += (self.df.iloc[self.day,-1]*min(abs(action),self.state[1]) * \
                            (1- TRANSACTION_FEE_PERCENT)).item()
            self.cost +=self.df.iloc[self.day,-1]*min(abs(action),self.state[1]) * \
                            TRANSACTION_FEE_PERCENT
            self.state[1] -= (min(abs(action), self.state[1]))
            self.trades+=1
        else:
            pass

    def _buy_stock(self,action):
        # perform buy action based on the sign of the action
        available_amount = self.state[0] // self.df.iloc[self.day,-1]
        # print('available_amount:{}'.format(available_amount))

        #update balance
        self.state[0] -= (self.df.iloc[self.day,-1]*min(available_amount, action)* \
                          (1+ TRANSACTION_FEE_PERCENT)).item()

        self.state[1] += (min(available_amount, action))

        self.cost+=self.df.iloc[self.day,-1]*min(available_amount, action)* \
                          TRANSACTION_FEE_PERCENT
        self.trades+=1

    def step(self,action):
        self.terminal = self.day >= len(self.df.Date.unique()) - 1

        if self.terminal:
            plt.plot(self.asset_memory,'r')
            plt.savefig('results/account_value_train.png')
            plt.close()

            df_total_value = pd.DataFrame(self.asset_memory)
            df_total_value.to_csv('results/account_value_train.csv')

            df_total_value.columns = ['account_value']
            df_total_value['daily_return'] = df_total_value.pct_change(1)
            
            df_rewards = pd.DataFrame(self.rewards_memory)
            
            return self.state, self.reward*REWARD_SCALING,self.terminal, {}

        else:
            # print(np.array(self.state[1:29]))

            action = action * HMAX_NORMALIZE
            #actions = (actions.astype(int))
            
            begin_total_asset = self.state[0]+ self.state[1]*self.df.iloc[self.day,-1]
            
            if action<0:
                self._sell_stock( action)
            else:
                self._buy_stock(action)

            self.day += 1        
            #load next state
            # print("stock_shares:{}".format(self.state[29:]))

            self.state = [self.state[0]] + [self.state[1]] + self.df.iloc[self.day-N:self.day,1].tolist() + \
                        self.df.iloc[self.day-N:self.day,2].tolist() + self.df.iloc[self.day-N:self.day,3].tolist() + \
                        self.df.iloc[self.day-N:self.day,4].tolist() + self.df.iloc[self.day-N:self.day,5].tolist() + \
                        self.df.iloc[self.day-N:self.day,6].tolist() + self.df.iloc[self.day-N:self.day,7].tolist()
            
            end_total_asset = self.state[0]+ self.state[1]*self.df.iloc[self.day,-1]

            try:
                self.asset_memory.append(end_total_asset.item())
            except:
                self.asset_memory.append(end_total_asset)

            #print("end_total_asset:{}".format(end_total_asset))
            
            self.reward = end_total_asset - begin_total_asset            
            self.rewards_memory.append(self.reward)
            self.reward = self.reward*REWARD_SCALING
            
        return np.array([self.state]),np.array([self.reward]),self.terminal,{}

    
    def reset(self):
        self.asset_memory = [INITIAL_ACCOUNT_BALANCE]
        self.day = 374
        self.cost = 0
        self.trades = 0
        self.terminal = False
        self.rewards_memory = []

        self.state = [INITIAL_ACCOUNT_BALANCE] + [0] + self.df.iloc[self.day-N:self.day,1].tolist() + \
                        self.df.iloc[self.day-N:self.day,2].tolist() + self.df.iloc[self.day-N:self.day,3].tolist() + \
                        self.df.iloc[self.day-N:self.day,4].tolist() + self.df.iloc[self.day-N:self.day,5].tolist() + \
                        self.df.iloc[self.day-N:self.day,6].tolist() + self.df.iloc[self.day-N:self.day,7].tolist()
        return self.state

    def render(self,mode='human'):
        return self.state

    def _seed(self,seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]