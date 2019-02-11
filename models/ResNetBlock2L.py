class ResNetBlock2L(nn.Module):
  
  def __init__(self, ic_conv1, oc_conv1, downsample):
    '''
    '''
    
    super().__init__()
    
    assert(downsample == True or downsample == False)
    self.downsample = downsample
    
    stride = 1
    if self.downsample:
        stride = 2
    
    self.conv1 = BNConv(in_channels=ic_conv1,
                        out_channes=oc_conv1,
                        kernel_size=3,
                        padding=1,
                        stride=stride)
    
    self.conv2 = BNConv(in_channels=oc_conv1,
                        out_channels=oc_conv1,
                        kernel_size=3,
                        padding=1,
                        stride=1)

    self.convs = BNConv(in_channels=ic_conv1,
                        out_channels=oc_conv1
                        kernel_size=3,
                        padding=1,
                        stride=stride)
    
    self.relu = nn.ReLU()
    
  def forward(self, x):
    '''
    '''
    
    xm = self.relu(self.conv1(x))
    xm = self.relu(self.conv2(xm))
    xm = self.conv3(xm)
    
    xs = self.convs(x) if self.downsample else x
    
    x = xm + xs
    x = self.relu(x)
    
    return x
