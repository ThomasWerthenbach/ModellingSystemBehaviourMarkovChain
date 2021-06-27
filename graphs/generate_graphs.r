library(ggplot2)
library(readr)
library(readxl)
library(tidyquant)

accuracy <- read_excel("accuracy.xlsx")
ggplot(data=accuracy, aes(x=compression, y=Value)) +
  geom_ma(aes(y=recall), ma_fun = SMA, n = 75, lwd=0.75, color="#999999", linetype = "solid") +
  geom_ma(aes(y=specificity), ma_fun = SMA, n = 75, lwd=0.75, color="#56B4E9", linetype = "solid") +
  geom_ma(aes(y=precision), ma_fun = SMA, n = 75, lwd=0.75, color="#D55E00", linetype = "solid") +
  geom_ma(aes(y=fmeasure), ma_fun = SMA, n = 75, lwd=0.75, color="#E69F00", linetype = "solid") +
  annotate("text", label="Specificity", x=110, y=0.01, size=3) +
  annotate("text", label="Recall", x=108, y=1, size=3) +
  annotate("text", label="Precision", x=109.5, y=0.5, size=3) +
  annotate("text", label="F-measure", x=110, y=0.67, size=3) +
  annotate("text", label="", x=115, y=0.67) +
  theme_bw() +
  xlab("Compression (%)") +
  scale_x_continuous(breaks = seq(0, 100, 10)) +
  scale_y_continuous(breaks = seq(0, 1, 0.1))
ggsave(filename="accuracy_results.pdf", device="pdf", width=12, height=8, units = "cm")


random <- read_excel("random.xlsx")
ggplot(data=random, aes(x=compression, y=Value)) +
  geom_ma(aes(y=recall), ma_fun = SMA, n = 75, lwd=0.75, color="#999999", linetype = "solid") +
  geom_ma(aes(y=specificity), ma_fun = SMA, n = 75, lwd=0.75, color="#56B4E9", linetype = "solid") +
  geom_ma(aes(y=precision), ma_fun = SMA, n = 75, lwd=0.75, color="#D55E00", linetype = "solid") +
  geom_ma(aes(y=fmeasure), ma_fun = SMA, n = 75, lwd=0.75, color="#E69F00", linetype = "solid") +
  annotate("text", label="Specificity", x=110, y=0.01, size=3) +
  annotate("text", label="Recall", x=108, y=1, size=3) +
  annotate("text", label="Precision", x=109.5, y=0.5, size=3) +
  annotate("text", label="F-measure", x=110, y=0.67, size=3) +
  annotate("text", label="", x=115, y=0.67) +
  theme_bw() +
  xlab("Compression (%)") +
  scale_x_continuous(breaks = seq(0, 100, 10)) +
  scale_y_continuous(breaks = seq(0, 1, 0.1))
ggsave(filename="random_results.pdf", device="pdf", width=12, height=8, units = "cm")

runtime <- read_excel("runtime.xlsx")
coefs <- coef(lm(seconds ~ dataset, data = runtime))
ggplot(data=runtime, aes(x=dataset, y=seconds, group=dataset)) +
  geom_boxplot(lwd=0.1, outlier.size=0.5) +
  theme_bw() +
  xlab("Size of dataset") +
  ylab("Time (s)") +
  geom_abline(intercept = coefs[1], slope = coefs[2]) +
  scale_x_continuous(breaks = seq(0, 1050, 100)) +
  scale_y_continuous(breaks = seq(0, 400, 50))
ggsave(filename="runtime_results.pdf", device="pdf", width=12, height=8, units = "cm")
