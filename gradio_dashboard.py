from fr_func import *
import gradio as gr

input = gr.inputs.Image()
output= gr.outputs.Image()

gr.Interface(fn= face_recog, inputs= input,
	outputs= output).launch(share = False)
