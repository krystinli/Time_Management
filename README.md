# Time_Management
> Goals are good for setting a direction, but systems are best for making progress.

This repo is designed to track my time management in these 3 areas: **work, development, and self-care**. I want to make sure I invest a bit in each of these 3 areas everyday for a good habit formation. 

## 01_How does it work?
I set up an expecation for the current monitoring period (outlined [here](https://github.com/krystinli/Time_Management/blob/main/run.py#L69-L75)) and then update hours spent with my actual performance of the day. The embedded logic computes a performance rating by comparing my goal vs. my actual performance. A positive rating means I'm hitting the target; a negative rating means I did not. 
- **Performance rating:** `Performance = Expected Hours - Actual Hours`
- **Overall goal:** To meet my target consistenly 📈

![img](https://getlighthouse.com/blog/wp-content/uploads/2016/03/dilbert_career_path.png)

## 02_Trends 
**Look back period:** 20 days <br/>

**Total hours** 🎯 spent in all 3 categories: this is an aggregated indicator of my overall performance
![total](https://github.com/krystinli/Time_Management/blob/main/img/total_plot.png)

### Work-Work 💻 - Work related tasks completion
Meetings and plannings don't count 👀. The idea is actually getting something done ✅
![work](https://github.com/krystinli/Time_Management/blob/main/img/work_plot.png)

### Development 🌳 - Investing in my growth
Personal projects, time spent on learnings outside of work 📚, and financial growth 💰
![coding](https://github.com/krystinli/Time_Management/blob/main/img/dev_plot.png)

### Self-Care 💟 - Prioritize my well-being
Exercising, meditation, planning, etc. 🏡 🏃‍♀️ 
![planning](https://github.com/krystinli/Time_Management/blob/main/img/care_plot.png)

## 03_Breakdown
Additional tracking for this month [here](https://github.com/krystinli/Time_Management/tree/main/Breakdown_Analysis).

### Workout 🏋️‍♀️
![img](https://github.com/krystinli/Time_Management/blob/main/img/2022_Apr_Tracking.png)


## 04_Pipeline
How are these plots generated? 📊
```mermaid
graph LR;
    A[Historical Data] --> B[New Dataset]
    E[New Activities] --> B[New Dataset]
    B[Updated Data] --> C[Transformed Data]
    C[Transformed Data] --> D[Plots]
```
