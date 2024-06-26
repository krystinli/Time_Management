# Time_Management
> Goals are good for setting a direction, but systems are best for making progress.

This repo is designed to track my time spent in 3 areas: **work, development, and self-care**. A healthy balance in these 3 areas can help achiving the most optimal outcome. Once you understand that habits can change, you have the freedom and the responsibility to remake them.

## 01_How does it work?
I set up an expecation for the current monitoring period (outlined [here](https://github.com/krystinli/Time_Management/blob/main/run.py#L77-L86)) and then update hours spent with my actual performance of the day. The embedded logic computes a performance rating by comparing my goal vs. my actual performance. A positive rating means I'm hitting the target; a negative rating means I did not. 

Every once a while I look at my performance in the past 2 weeks and evaluate the month over month trend. This helps me coming up with a more realistic expectation for the next time period. 
- **Performance rating:** `Performance = Expected Hours - Actual Hours`
- **Overall goal:** To meet my target consistenly 📈

![img](https://getlighthouse.com/blog/wp-content/uploads/2016/03/dilbert_career_path.png)

## 02_Trends 

### Total hours 📊
Sum of all 3 categories: this is an aggregated indicator of my overall performance
 
![total](https://github.com/krystinli/Time_Management/blob/main/img/total_plot.png)

Avg 4 weeks/month, 50 hrs / week => 200 hrs target 🎯
![total_monthly](https://github.com/krystinli/Time_Management/blob/main/img/total_plot_monthly.png)

### Work-Work 💻 - Work related tasks completion
Meetings and plannings don't count 👀. The idea is actually getting something done ✅

![work](https://github.com/krystinli/Time_Management/blob/main/img/work_plot.png)

![work_monthly](https://github.com/krystinli/Time_Management/blob/main/img/work_plot_monthly.png)

### Development 🌳 - Investing in my growth
Personal projects, time spent on learnings outside of work 📚, and financial growth 💰
![coding](https://github.com/krystinli/Time_Management/blob/main/img/dev_plot.png)

![dev_monthly](https://github.com/krystinli/Time_Management/blob/main/img/dev_plot_monthly.png)

### Self-Care 💟 - Prioritize my well-being
Exercising, meditation, planning, etc. 🏡 🏃‍♀️ 
![planning](https://github.com/krystinli/Time_Management/blob/main/img/care_plot.png)

![care_monthly](https://github.com/krystinli/Time_Management/blob/main/img/care_plot_monthly.png)


## 03_Pipeline
How are these plots generated? 📊
```mermaid
graph LR;
    A[Historical Data] --> B[New Dataset]
    E[New Activities] --> B[New Dataset]
    B[Updated Data] --> C[Transformed Data]
    C[Transformed Data] --> D[Plots]
```
