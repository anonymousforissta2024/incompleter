#Source: https://stackoverflow.com/questions/55878788/how-to-fix-attributeerror-module-chart-studio-tools-has-no-attribute-make-s
calls.set_index('STRIKE_PRC')[['CF_CLOSE', 'IMP_VOLT']].iplot(subplots=True,
                                                             mode='lines+markers',size=6)