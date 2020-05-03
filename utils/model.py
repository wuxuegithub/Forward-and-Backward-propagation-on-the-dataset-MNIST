# LeNet5 object
import numpy


class LeNet5(object):

    def softmax(self, Z):
        expZ = numpy.np.exp(Z - numpy.np.max(Z))
        return expZ / expZ.sum(axis=0, keepdims=True)

    def crossentropy(pred,real):
        res=pred-real
        return res

    def relu_deri(self,Z):
        if (Z>0):
            return 1
        else:
            return 0


    def maxpooling (feature_map,size=2,stride=2):
        #declare an empty array for storing the output
        pool=numpy.zeros(numpy.unit16((feature_map.shape[0]-size+1)/stride),
                         numpy.uint16((feature_map.shape[1]-size+1)/stride),
                         numpy.unit16(feature_map.shape[-1]))
        for map_num in feature_map.shape[-1]:
            r2=0
            for r in numpy.arrange(0,feature_map.shape[0]-size-1,stride):
                c2=0
                for c in numpy.arrange(0,feature_map.shape[1]-size-1,stride):
                    pool[r2,c2,map_num]=numpy.max([feature_map[r:r+size,c:c+size,map_num]])
                    c2=c2+1
            r2=r2+1
        return pool
    def relu(feature_map):
        reluout=numpy.zero(feature_map.shape)
        for map_num in feature_map.shape[-1]:
            for r in numpy.arrange(0,feature_map.shape[0]):
                for c in numpy.arrange(0,feature_map.shape[1]):
                    reluout[r,c,map_num]=numpy.max([feature_map[r,c,map_num]])

        return reluout


    def fc6(feature_map):
        return feature_map.reshape(84,1)

    def fc7(feature_map):
        return feature_map.reshape(10,1)


    # convolution layer
    def convolution(input_image, filt, no_filter, bias, filter_size=5, stride=1):

        depth, input_dim, _ = input_image.shape  # image dimensions
        out_dim = int((input_dim - filter_size) / stride) + 1  # calculate output dimensions
        #print(out_dim)
        convout = numpy.zeros((no_filter, out_dim, out_dim))

        # convolve each filter over the image
        for f in range(no_filter):
            height = 0
            # move filter vertically across the image
            while height + filter_size <= input_dim:
                width = 0
                # move filter horizontally across the image
                while width + filter_size <= input_dim:
                    # perform the convolution operation and add the bias
                    convout[f, height, width] = numpy.sum(filt[f] * input_image[:, height:height+filter_size, width:width+filter_size]) + bias[width]
                    width += stride
                height += stride

        return convout








    def __init__(self):
        # YOUR IMPLEMETATION
        #define our layers

        raise NotImplementedError

    def Forward_Propagation(self, input_image, input_label, mode):
        # YOUR IMPLEMETATION
        filtC1 = numpy.random.randn(6, 5, 5) / 25
        filtC3 = numpy.random.randn(16, 5, 5) / 25
        filtC5 = numpy.random.randn(120, 5, 5) / 25

        raise NotImplementedError

    def Back_Propagation(self, lr_global):
        # YOUR IMPLEMETATION
        a7_delta= self.crossentropy(self.a7,self.y)
        z6_delta=numpy.dot(a7_delta,self.w7)
        a6_delta=z6_delta*self.relu_deri(self,self.a6)
        z5_delta = numpy.dot(a6_delta, self.w6)
        a5_delta = z5_delta * self.relu_deri(self, self.a5)
        z4_delta = numpy.dot(a5_delta, self.w5)
        a4_delta = z4_delta * self.relu_deri(self, self.a4)
        z3_delta = numpy.dot(a4_delta, self.w4)
        a3_delta = z3_delta * self.relu_deri(self, self.a3)
        z2_delta = numpy.dot(a3_delta, self.w3)
        a2_delta = z2_delta * self.relu_deri(self, self.a2)
        z1_delta = numpy.dot(a2_delta, self.w2)
        a1_delta = z1_delta * self.relu_deri(self, self.x)

        self.w7 -= lr_global* numpy.dot(self.a6, a7_delta)
        self.w6 -= lr_global * numpy.dot(self.a5, a6_delta)
        self.w5 -= lr_global* numpy.dot(self.a4, a5_delta)
        self.w4 -= lr_global * numpy.dot(self.a3, a4_delta)
        self.w3 -= lr_global * numpy.dot(self.a2, a3_delta)
        self.w2 -= lr_global * numpy.dot(self.a1, a2_delta)
        self.w1 -= lr_global* numpy.dot(self.x, a1_delta)

