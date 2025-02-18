import derivative
import torch

def Loss_function(v_old, v_new, v_cond, flow_mask, cond_mask):
    v = (v_new + v_old) / 2
    loss_mom = torch.mean(torch.pow(flow_mask * (rho * ((v_new[:,1:2] - v_old[:,1:2])/dt + v[:,1:2] * dx(v[:,1:2]) + 0.5 * (y2x_bottom(v[:,0:1]) * dy_bottom(v[:,0:1]) + y2x_top(v[:,0:1]) * dy_top(v[:, 0:1]))) + dx_left(p_new) - mu * laplace(v[:,1:2]), dim = (1,2,3)), 2)) + \
                torch.mean(torch.pow(flow_mask * (rho * (v_new[:,0:1] - v_old[:,0:1])/dt + v[:,0:1] * dy(v[:,0:1]) + 0.5 * (x2y_left(v[:,1:2]) * dx_left(v[:,1:2]) + x2y_right(v[:,1:2]) * dx_right(v[:,1:2])) + dy_bottom(p_new) - mu * laplace(v[:,0:1]))),2), dim = (1,2,3))
    
    loss_bdry = torch.mean(torch.pow(cond_mask * (v_new - v_cond),2),dim = (1,2,3))

    loss = loss_mom * mom_para + loss_bdry * mom_para

    return torch.mean(torch.log(loss))
                          


