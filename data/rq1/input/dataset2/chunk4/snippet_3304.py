#Source: https://stackoverflow.com/questions/75030446/attributeerror-kmeans-object-has-no-attribute-labels-pytorch
class KMeansInitMostDistantFromMean:
    def __call__(self, *args, **kwargs):
        X, k = args
        mean = np.mean(X, axis=0)
        arg_sorted = np.argsort(np.apply_along_axis(lambda y: euclidean(mean, y), 1, X))
        output = X[np.flip(arg_sorted)[:k]]
        return output

class KMeansInit:
    def __call__(self, *args, **kwargs):
        X, k = args
        current_centroids = np.expand_dims(np.mean(X, axis=0), 0)
        for i in range(k - 1):
            X, current_centroids = self.next_centroid(X, current_centroids)

        return current_centroids

    def next_centroid(self, X, curr_centroids):
        highest_dist = 0.0
        next_centroid = None
        next_centroid_index = None
        for i, x in enumerate(X):
            max_dist = np.amax(np.apply_along_axis(lambda y: euclidean(x, y), 1, curr_centroids))
            if max_dist > highest_dist:
                next_centroid = x
                highest_dist = max_dist
                next_centroid_index = i

        return np.delete(X, next_centroid_index, 0), np.append(curr_centroids, np.expand_dims(next_centroid, 0), 0)


class Conv(gnn.MessagePassing):
   
    def __init__(self, sigma: nn.Module, F: nn.Module, W: nn.Module, M: nn.Module, C: int, P: int):
       
        super().__init__(aggr="mean")
        self.sigma = sigma
        self.F = F
        self.W = W
        self.M = M
        self.C = C
        self.P = P
        self.B = torch.randn(C+P, requires_grad=True)

    def forward(self, feature_matrix, edge_index):
        return self.propagate(edge_index, feature_matrix=feature_matrix)

    def message(self, feature_matrix_i, feature_matrix_j):
        message = self.F(feature_matrix_j - feature_matrix_i)
        message = message.view(-1, self.C + self.P, self.C)
        feature_matrix_i_ = feature_matrix_i.unsqueeze(2)
        output = torch.bmm(message, feature_matrix_i_).squeeze()
        return output

    def update(self, aggr_out, feature_matrix):
        Weight = self.M(aggr_out)
        aggr_out = aggr_out * Weight
        transform = self.W(feature_matrix)
        transform = transform.view(-1, self.C + self.P, self.C)
        feature_matrix = feature_matrix.unsqueeze(2)
        transformation = torch.bmm(transform, feature_matrix).squeeze()
        aggr_out = aggr_out + transformation
        output = aggr_out + self.B
        output = self.sigma(output)
        return output


class Aggregation(nn.Module):
    
    def __init__(self, mlp1: nn.Module, mlp2: nn.Module):
       
        super().__init__()
        self.mlp1 = mlp1
        self.mlp2 = mlp2
        self.softmax = nn.Softmax(0)

    def forward(self, feature_matrix_batch: torch.Tensor, conv_feature_matrix_batch: torch.Tensor):
        N, I, D = feature_matrix_batch.size()
        N_, I_, D_ = conv_feature_matrix_batch.size()
        augmentation = D_ - D
        if augmentation > 0:
            feature_matrix_batch = F.pad(feature_matrix_batch, (0, augmentation))
        S1 = torch.mean(feature_matrix_batch, 1)
        S2 = torch.mean(conv_feature_matrix_batch, 1)
        Z1 = self.mlp1(S1)
        Z2 = self.mlp2(S2)
        M = self.softmax(torch.stack((Z1, Z2), 0))
        M1 = M[0]
        M2 = M[1]
        M1 = M1.unsqueeze(1).expand(-1, I, -1)
        M2 = M2.unsqueeze(1).expand(-1, I, -1)
        output = (M1 * feature_matrix_batch) + (M2 * conv_feature_matrix_batch)
        return output


class MaxPool(nn.Module):
    
    def __init__(self, k: int):
        
        super().__init__()
        self.k = k

    def forward(self, feature_matrix_batch: torch.Tensor, cluster_index: torch.Tensor):
       
        N, I, D = feature_matrix_batch.size()
        feature_matrix_batch = feature_matrix_batch.view(-1, D)
        output = scatter_max(feature_matrix_batch, cluster_index, dim=0)[0]
        output = output.view(N, self.k, -1)
        
        return output


class GraphConvPool3DPnet(nn.Module):
    
    def __init__(self, shrinkingLayers: [ShrinkingUnit], mlp: nn.Module):
        super().__init__()
        self.neuralNet = nn.Sequential(*shrinkingLayers, mlp)

    def forward(self, x: torch.Tensor, pos: torch.Tensor):
        feature_matrix_batch = torch.cat((pos, x), 2) if x is not None else pos
        return self.neuralNet(feature_matrix_batch)

class ShrinkingUnitStack(nn.Module):
   
    def __init__(self, input_stack: int, stack_fork: int, mlp: nn.Module, learning_rate: int, k: int, kmeansInit, n_init, sigma: nn.Module, F: nn.Module, W: nn.Module,
                 M: nn.Module, C, P, mlp1: nn.Module, mlp2: nn.Module):
       
        super().__init__()
        self.stack_fork = stack_fork
        stack_size = input_stack * stack_fork
        self.selfCorrStack = SelfCorrelationStack(stack_size, mlp, learning_rate)
        self.kmeansConvStack = KMeansConvStack(stack_size, k, kmeansInit, n_init, sigma, F, W, M, C, P)
        self.localAdaptFeaAggreStack = AggregationStack(stack_size, mlp1, mlp2)
        self.graphMaxPoolStack = MaxPoolStack(stack_size, k)

    def forward(self, feature_matrix_batch):
        
        feature_matrix_batch = torch.repeat_interleave(feature_matrix_batch, self.stack_fork, dim=0)
        
        feature_matrix_batch = self.selfCorrStack(feature_matrix_batch)
        
        feature_matrix_batch_, conv_feature_matrix_batch, cluster_index = self.kmeansConvStack(feature_matrix_batch)
        feature_matrix_batch = self.localAdaptFeaAggreStack(feature_matrix_batch, conv_feature_matrix_batch)
        output = self.graphMaxPoolStack(feature_matrix_batch, cluster_index)
       
        return output


class SelfCorrelationStack(nn.Module):
   
    def __init__(self, stack_size: int, mlp: nn.Module, learning_rate: int = 1.0):
       
        super().__init__()
        self.selfCorrelationStack = nn.ModuleList([SelfCorrelation(copy.deepcopy(mlp), learning_rate) for i in range(stack_size)])
        self.apply(init_weights)

    def forward(self, feature_matrix_batch: torch.Tensor):
        # feature_matrix_batch size = (S,N,I,D) where S=stack_size, N=batch number, I=members, D=member dimensionality
        output = selfCorrThreader(self.selfCorrelationStack, feature_matrix_batch)
        # output size = (S,N,I,D) where where S=stack_size, N=batch number, I=members, D=member dimensionality
        return output


class KMeansConvStack(nn.Module):
    
    def __init__(self, stack_size: int, k: int, kmeansInit, n_init: int, sigma: nn.Module, F: nn.Module, W: nn.Module,
                 M: nn.Module, C: int, P: int):
        
        super().__init__()
        self.kmeansConvStack = nn.ModuleList([
            KMeansConv(k, kmeansInit, n_init, copy.deepcopy(sigma), copy.deepcopy(F), copy.deepcopy(W),
                       copy.deepcopy(M), C, P) for i in range(stack_size)])
        self.apply(init_weights)

    def forward(self, feature_matrix_batch: torch.Tensor):
        # feature_matrix_batch size = (S,N,I,D) where S=stack size, N=batch number, I=members, D=member dimensionality
        feature_matrix_batch, conv_feature_matrix_batch, cluster_index = kmeansConvThreader(self.kmeansConvStack,
                                                                                            feature_matrix_batch)
  
        return feature_matrix_batch, conv_feature_matrix_batch, cluster_index


class AggregationStack(nn.Module):
    
    def __init__(self, stack_size: int, mlp1: nn.Module, mlp2: nn.Module):
       
        super().__init__()
        self.localAdaptFeatAggreStack = nn.ModuleList([Aggregation(copy.deepcopy(mlp1), copy.deepcopy(mlp2)) for i
                                                       in range(stack_size)])
        self.apply(init_weights)

    def forward(self, feature_matrix_batch: torch.Tensor, conv_feature_matrix_batch: torch.Tensor):
        
        output = threader(self.localAdaptFeatAggreStack, feature_matrix_batch, conv_feature_matrix_batch)
        
        return output


class MaxPoolStack(nn.Module):
    
    def __init__(self, stack_size: int, k: int):
        
        super().__init__()
        self.graphMaxPoolStack = nn.ModuleList([MaxPool(k) for i in range(stack_size)])
        self.apply(init_weights)

    def forward(self, feature_matrix_batch: torch.Tensor, cluster_index: torch.Tensor):
        
        output = threader(self.graphMaxPoolStack, feature_matrix_batch, cluster_index)
       
        return output


def selfCorrThreader(modules, input_tensor):
    list_append = []
    threads = []
    for i, t in enumerate(input_tensor):
        threads.append(Thread(target=selfCorrAppender, args=(modules[i], t, list_append, i)))
    [t.start() for t in threads]
    [t.join() for t in threads]
    list_append.sort()
    list_append = list(map(lambda x: x[1], list_append))
    return torch.stack(list_append)


def selfCorrAppender(module, tensor, list_append, index):
    list_append.append((index, module(tensor)))


def kmeansConvThreader(modules, input_tensor):
    list1_append = []
    list2_append = []
    list3_append = []
    threads = []
    for i, t in enumerate(input_tensor):
        threads.append(
            Thread(target=kmeansAppender, args=(modules[i], t, list1_append, list2_append, list3_append, i)))
    [t.start() for t in threads]
    [t.join() for t in threads]
    list1_append.sort()
    list2_append.sort()
    list3_append.sort()
    list1_append = list(map(lambda x: x[1], list1_append))
    list2_append = list(map(lambda x: x[1], list2_append))
    list3_append = list(map(lambda x: x[1], list3_append))
    return torch.stack(list1_append), torch.stack(list2_append), torch.stack(list3_append)


def kmeansAppender(module, input, list1_append, list2_append, list3_append, index):
    x, y, z = module(input)
    list1_append.append((index, x))
    list2_append.append((index, y))
    list3_append.append((index, z))


def threader(modules, input_tensor1, input_tensor2):
    list_append = []
    threads = []
    for i, t in enumerate(input_tensor1):
        threads.append(Thread(target=threaderAppender, args=(modules[i], t, input_tensor2[i], list_append, i)))
    [t.start() for t in threads]
    [t.join() for t in threads]
    list_append.sort()
    list_append = list(map(lambda x: x[1], list_append))
    return torch.stack(list_append)


def threaderAppender(module, t1, t2, list_append, index):
    list_append.append((index, module(t1, t2)))


class Classifier(nn.Module):
    
    def __init__(self, shrinkingLayersStack: [ShrinkingUnitStack], mlp: nn.Module):
       
        super().__init__()
        self.neuralNet = nn.Sequential(*shrinkingLayersStack)
        self.mlp = mlp

    def forward(self, x: torch.Tensor, pos: torch.Tensor):
       
        feature_matrix_batch = pos.unsqueeze(0)
        
        output = self.neuralNet(feature_matrix_batch)
        
        output = torch.mean(output, dim=0)
        
        return self.mlp(output)