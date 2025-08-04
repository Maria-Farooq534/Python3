{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4f9f6843",
   "metadata": {},
   "outputs": [
    {
     "ename": "Terminator",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTerminator\u001b[39m                                Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 5\u001b[39m\n\u001b[32m      2\u001b[39m wn = turtle.Screen()\n\u001b[32m      3\u001b[39m wn.bgcolor(\u001b[33m\"\u001b[39m\u001b[33mlightblue\u001b[39m\u001b[33m\"\u001b[39m)\n\u001b[32m----> \u001b[39m\u001b[32m5\u001b[39m alex = \u001b[43mturtle\u001b[49m\u001b[43m.\u001b[49m\u001b[43mTurtle\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m      6\u001b[39m alex.pencolor(\u001b[33m\"\u001b[39m\u001b[33mred\u001b[39m\u001b[33m\"\u001b[39m)\n\u001b[32m      7\u001b[39m alex.pensize(\u001b[32m5\u001b[39m)\n",
      "\u001b[36mFile \u001b[39m\u001b[32mc:\\Users\\Ali\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\turtle.py:3845\u001b[39m, in \u001b[36mTurtle.__init__\u001b[39m\u001b[34m(self, shape, undobuffersize, visible)\u001b[39m\n\u001b[32m   3843\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m Turtle._screen \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[32m   3844\u001b[39m     Turtle._screen = Screen()\n\u001b[32m-> \u001b[39m\u001b[32m3845\u001b[39m \u001b[43mRawTurtle\u001b[49m\u001b[43m.\u001b[49m\u001b[34;43m__init__\u001b[39;49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mTurtle\u001b[49m\u001b[43m.\u001b[49m\u001b[43m_screen\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   3846\u001b[39m \u001b[43m                   \u001b[49m\u001b[43mshape\u001b[49m\u001b[43m=\u001b[49m\u001b[43mshape\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   3847\u001b[39m \u001b[43m                   \u001b[49m\u001b[43mundobuffersize\u001b[49m\u001b[43m=\u001b[49m\u001b[43mundobuffersize\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   3848\u001b[39m \u001b[43m                   \u001b[49m\u001b[43mvisible\u001b[49m\u001b[43m=\u001b[49m\u001b[43mvisible\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32mc:\\Users\\Ali\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\turtle.py:2564\u001b[39m, in \u001b[36mRawTurtle.__init__\u001b[39m\u001b[34m(self, canvas, shape, undobuffersize, visible)\u001b[39m\n\u001b[32m   2562\u001b[39m \u001b[38;5;28mself\u001b[39m._undobuffersize = undobuffersize\n\u001b[32m   2563\u001b[39m \u001b[38;5;28mself\u001b[39m.undobuffer = Tbuffer(undobuffersize)\n\u001b[32m-> \u001b[39m\u001b[32m2564\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43m_update\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32mc:\\Users\\Ali\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\turtle.py:2667\u001b[39m, in \u001b[36mRawTurtle._update\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m   2665\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m\n\u001b[32m   2666\u001b[39m \u001b[38;5;28;01melif\u001b[39;00m screen._tracing == \u001b[32m1\u001b[39m:\n\u001b[32m-> \u001b[39m\u001b[32m2667\u001b[39m     \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43m_update_data\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m   2668\u001b[39m     \u001b[38;5;28mself\u001b[39m._drawturtle()\n\u001b[32m   2669\u001b[39m     screen._update()                  \u001b[38;5;66;03m# TurtleScreenBase\u001b[39;00m\n",
      "\u001b[36mFile \u001b[39m\u001b[32mc:\\Users\\Ali\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\turtle.py:2653\u001b[39m, in \u001b[36mRawTurtle._update_data\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m   2652\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34m_update_data\u001b[39m(\u001b[38;5;28mself\u001b[39m):\n\u001b[32m-> \u001b[39m\u001b[32m2653\u001b[39m     \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mscreen\u001b[49m\u001b[43m.\u001b[49m\u001b[43m_incrementudc\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m   2654\u001b[39m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m.screen._updatecounter != \u001b[32m0\u001b[39m:\n\u001b[32m   2655\u001b[39m         \u001b[38;5;28;01mreturn\u001b[39;00m\n",
      "\u001b[36mFile \u001b[39m\u001b[32mc:\\Users\\Ali\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\turtle.py:1283\u001b[39m, in \u001b[36mTurtleScreen._incrementudc\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m   1281\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m TurtleScreen._RUNNING:\n\u001b[32m   1282\u001b[39m     TurtleScreen._RUNNING = \u001b[38;5;28;01mTrue\u001b[39;00m\n\u001b[32m-> \u001b[39m\u001b[32m1283\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m Terminator\n\u001b[32m   1284\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m._tracing > \u001b[32m0\u001b[39m:\n\u001b[32m   1285\u001b[39m     \u001b[38;5;28mself\u001b[39m._updatecounter += \u001b[32m1\u001b[39m\n",
      "\u001b[31mTerminator\u001b[39m: "
     ]
    },
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mThe Kernel crashed while executing code in the current cell or a previous cell. \n",
      "\u001b[1;31mPlease review the code in the cell(s) to identify a possible cause of the failure. \n",
      "\u001b[1;31mClick <a href='https://aka.ms/vscodeJupyterKernelCrash'>here</a> for more info. \n",
      "\u001b[1;31mView Jupyter <a href='command:jupyter.viewOutput'>log</a> for further details."
     ]
    }
   ],
   "source": [
    "import turtle\n",
    "wn = turtle.Screen()\n",
    "wn.bgcolor(\"lightblue\")\n",
    "\n",
    "alex = turtle.Turtle()\n",
    "alex.pencolor(\"red\")\n",
    "alex.pensize(5)\n",
    "\n",
    "alex.penup()\n",
    "for _ in range(10):\n",
    "    alex.stamp()\n",
    "    alex.forward(50)\n",
    "    alex.right(34)\n",
    "\n",
    "\n",
    "wn.exitonclick()\n"
   ]
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
   "version": "3.13.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
