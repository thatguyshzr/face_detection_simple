from fr_func import *
import gradio as gr

input = gr.inputs.Image()
output= gr.outputs.Image()
scale_factor = gr.inputs.Slider(minimum= 0.8, maximum =2.0,
	step= 0.1, default= 1.1, label= 'Scale Factor')

gr.Interface(fn= face_recog, inputs= input,
	outputs= output).launch()
