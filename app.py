<<<<<<< HEAD
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 验证函数
def validate_step0(answer): return answer == "开始寻宝"
def validate_step1(answer): return answer in ["致远", "致远学院"]
def validate_step2(answer): return answer == "清明上河图"
def validate_step3(answer): return answer in ["包图", "包玉刚图书馆"]
def validate_step4(answer): return ("学森" in answer) and ("元培" in answer)
def validate_step5(answer): return answer == "梦想注点"

VALIDATORS = [validate_step0, validate_step1, validate_step2, validate_step3, validate_step4, validate_step5]

@app.route('/api/validate', methods=['POST'])
def validate():
    data = request.get_json()
    user_answer = data.get('answer', '').strip()
    step = data.get('step', 0)
    if step < 0 or step >= len(VALIDATORS):
        return jsonify({"correct": False, "message": "无效步骤"})
    if VALIDATORS[step](user_answer):
        new_step = step + 1
        finished = (new_step >= len(VALIDATORS))
        return jsonify({"correct": True, "finished": finished, "message": "正确！", "new_step": new_step})
    else:
        return jsonify({"correct": False, "message": "答案错误"})

# 推理内容（通关后显示）
REASONING_HTML = """
<ol>
    <li>“文至心达”表示“文”在“至”旁，为“致”；“千里始行”表明从元点开始处走，为“远”。故字谜谜底为“致远”，需要玩家到致远学院寻找线索。</li>
    <li>图中有24种花，分别对应二十四节气，其中唯一一个上色的是第五个，桐花，对应节气为“清明”。在致远学院二楼走廊的一个自习隔间内挂有剪纸作品《清明上河图》。故谜底为“清明上河图”。</li>
    <li>新定义运算，运算符号“：”提示运算逻辑和时间有关，运算结果“（x，y）”提示结果代表的是坐标。观察几个样例发现，新定义运算a：b是先将两数相乘，再将结果转化为60进制的时间，得到结果（06,04）和（12,05）。在清明上河图的介绍标签右上角贴有一个小的坐标轴，得到坐标对应的字为“包”和“图”（符号不计字数）。故谜底为“包图”。</li>
    <li>根据文字提示，这题要寻找的是两条路的名字，由包图一进门的钱学森先生的名言“图书馆是我每天必去的地方”，推断出其中一条路是“学森路”；根据图片提示，地图中的包图下方有英文名“Yue-kong Pao Library”的大写字母“YPL”得到校内唯一一条对应首字母的路“元培路”。故谜底为“学森”和“元培”。</li>
    <li>根据图片提示，为百度地图的图标，提示要看地图，结合上一题得到的学森路和元培路，观察地图可以发现，两条路之间只有东中院和东下院。容易找到东下院庭中形似百度地图的图标的红色雕塑。如果认真看了《清明上河图》剪纸作品的介绍，也可以发现作者是中国科学院院士，联想到东下院院士墙。故谜底为雕塑正面的“梦想注点”。</li>
</ol>
<p style="margin-top:0.8rem; font-style:italic;">—— 猫猫的推理笔记 🐾</p>
"""

@app.route('/api/reasoning', methods=['GET'])
def get_reasoning():
    return jsonify({"html": REASONING_HTML})

if __name__ == '__main__':
=======
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 验证函数
def validate_step0(answer): return answer == "开始寻宝"
def validate_step1(answer): return answer in ["致远", "致远学院"]
def validate_step2(answer): return answer == "清明上河图"
def validate_step3(answer): return answer in ["包图", "包玉刚图书馆"]
def validate_step4(answer): return ("学森" in answer) and ("元培" in answer)
def validate_step5(answer): return answer == "梦想注点"

VALIDATORS = [validate_step0, validate_step1, validate_step2, validate_step3, validate_step4, validate_step5]

@app.route('/api/validate', methods=['POST'])
def validate():
    data = request.get_json()
    user_answer = data.get('answer', '').strip()
    step = data.get('step', 0)
    if step < 0 or step >= len(VALIDATORS):
        return jsonify({"correct": False, "message": "无效步骤"})
    if VALIDATORS[step](user_answer):
        new_step = step + 1
        finished = (new_step >= len(VALIDATORS))
        return jsonify({"correct": True, "finished": finished, "message": "正确！", "new_step": new_step})
    else:
        return jsonify({"correct": False, "message": "答案错误"})

# 推理内容（通关后显示）
REASONING_HTML = """
<ol>
    <li>“文至心达”表示“文”在“至”旁，为“致”；“千里始行”表明从元点开始处走，为“远”。故字谜谜底为“致远”，需要玩家到致远学院寻找线索。</li>
    <li>图中有24种花，分别对应二十四节气，其中唯一一个上色的是第五个，桐花，对应节气为“清明”。在致远学院二楼走廊的一个自习隔间内挂有剪纸作品《清明上河图》。故谜底为“清明上河图”。</li>
    <li>新定义运算，运算符号“：”提示运算逻辑和时间有关，运算结果“（x，y）”提示结果代表的是坐标。观察几个样例发现，新定义运算a：b是先将两数相乘，再将结果转化为60进制的时间，得到结果（06,04）和（12,05）。在清明上河图的介绍标签右上角贴有一个小的坐标轴，得到坐标对应的字为“包”和“图”（符号不计字数）。故谜底为“包图”。</li>
    <li>根据文字提示，这题要寻找的是两条路的名字，由包图一进门的钱学森先生的名言“图书馆是我每天必去的地方”，推断出其中一条路是“学森路”；根据图片提示，地图中的包图下方有英文名“Yue-kong Pao Library”的大写字母“YPL”得到校内唯一一条对应首字母的路“元培路”。故谜底为“学森”和“元培”。</li>
    <li>根据图片提示，为百度地图的图标，提示要看地图，结合上一题得到的学森路和元培路，观察地图可以发现，两条路之间只有东中院和东下院。容易找到东下院庭中形似百度地图的图标的红色雕塑。如果认真看了《清明上河图》剪纸作品的介绍，也可以发现作者是中国科学院院士，联想到东下院院士墙。故谜底为雕塑正面的“梦想注点”。</li>
</ol>
<p style="margin-top:0.8rem; font-style:italic;">—— 猫猫的推理笔记 🐾</p>
"""

@app.route('/api/reasoning', methods=['GET'])
def get_reasoning():
    return jsonify({"html": REASONING_HTML})

if __name__ == '__main__':
>>>>>>> afc1bccc5eccb8e301bef45c1322faeb7d9c537b
    app.run(host='0.0.0.0', port=5000)