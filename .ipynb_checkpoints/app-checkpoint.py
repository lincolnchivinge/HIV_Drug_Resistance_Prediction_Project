{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "convert the model into a character stream using pickling. This character stream contains all the information necessary to reconstruct the object in another python script."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# importing libraries\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import pickle\n",
    "import flask\n",
    "from flask import Flask, request, jsonify, render_template"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Initialize the flask App\n",
    "app = Flask(__name__)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### The next part makes an API which receives factors details through GUI and computes the predicted Drug Resistance value based on model. De- serialize the pickled model in the form of python object. Set the main page using index.html. On submitting the form values using POST request to /predict, we get the predicted Drug Resistance value. The results can be shown by making another POST request to /results. It receives JSON inputs, uses the trained model to make a prediction and returns that prediction in JSON format which can be accessed through the API endpoint."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "[2021-07-27 23:23:20,062] ERROR in app: Exception on / [GET]\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\ProgramData\\Anaconda3\\lib\\site-packages\\flask\\app.py\", line 2446, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "  File \"C:\\ProgramData\\Anaconda3\\lib\\site-packages\\flask\\app.py\", line 1951, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "  File \"C:\\ProgramData\\Anaconda3\\lib\\site-packages\\flask\\app.py\", line 1820, in handle_user_exception\n",
      "    reraise(exc_type, exc_value, tb)\n",
      "  File \"C:\\ProgramData\\Anaconda3\\lib\\site-packages\\flask\\_compat.py\", line 39, in reraise\n",
      "    raise value\n",
      "  File \"C:\\ProgramData\\Anaconda3\\lib\\site-packages\\flask\\app.py\", line 1949, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "  File \"C:\\ProgramData\\Anaconda3\\lib\\site-packages\\flask\\app.py\", line 1935, in dispatch_request\n",
      "    return self.view_functions[rule.endpoint](**req.view_args)\n",
      "  File \"<ipython-input-3-a52e0fcebfba>\", line 8, in home\n",
      "    return render_template('index.html')\n",
      "  File \"C:\\ProgramData\\Anaconda3\\lib\\site-packages\\flask\\templating.py\", line 138, in render_template\n",
      "    ctx.app.jinja_env.get_or_select_template(template_name_or_list),\n",
      "  File \"C:\\ProgramData\\Anaconda3\\lib\\site-packages\\jinja2\\environment.py\", line 930, in get_or_select_template\n",
      "    return self.get_template(template_name_or_list, parent, globals)\n",
      "  File \"C:\\ProgramData\\Anaconda3\\lib\\site-packages\\jinja2\\environment.py\", line 883, in get_template\n",
      "    return self._load_template(name, self.make_globals(globals))\n",
      "  File \"C:\\ProgramData\\Anaconda3\\lib\\site-packages\\jinja2\\environment.py\", line 857, in _load_template\n",
      "    template = self.loader.load(self, name, globals)\n",
      "  File \"C:\\ProgramData\\Anaconda3\\lib\\site-packages\\jinja2\\loaders.py\", line 117, in load\n",
      "    source, filename, uptodate = self.get_source(environment, name)\n",
      "  File \"C:\\ProgramData\\Anaconda3\\lib\\site-packages\\flask\\templating.py\", line 60, in get_source\n",
      "    return self._get_source_fast(environment, template)\n",
      "  File \"C:\\ProgramData\\Anaconda3\\lib\\site-packages\\flask\\templating.py\", line 89, in _get_source_fast\n",
      "    raise TemplateNotFound(template)\n",
      "jinja2.exceptions.TemplateNotFound: index.html\n",
      "127.0.0.1 - - [27/Jul/2021 23:23:20] \"\u001b[35m\u001b[1mGET / HTTP/1.1\u001b[0m\" 500 -\n"
     ]
    }
   ],
   "source": [
    "# prediction function initialization\n",
    "model = pickle.load(open('model.pkl', 'rb'))\n",
    "  \n",
    "    \n",
    "#default page of web-app\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return render_template('index.html')\n",
    "\n",
    "\n",
    "#To use the predict button in our web-app\n",
    "@app.route('/predict/<float:value>',methods=['POST'])\n",
    "def predict(value):\n",
    "    #For rendering results on HTML GUI\n",
    "    int_features = [float(x) for x in request.form.values()]\n",
    "    final_features = [np.array(int_features)]\n",
    "    prediction = model.predict(final_features)\n",
    "    output = round(prediction[0], 2) \n",
    "    return render_template('index.html', prediction_text='CO2    Emission of the vehicle is :{}'.format(output))\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=False)\n",
    "     \n",
    "        "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## RESULTS - Run the web application using command below"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#python app.py"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Open http://127.0.0.1:5000/ in web-browser, and the GUI as shown below should appear.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
