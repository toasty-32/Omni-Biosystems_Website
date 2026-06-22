interface LoadingSpinnerProps {
  size?: number
  message?: string
}

export default function LoadingSpinner({ size = 40, message }: LoadingSpinnerProps) {
  return (
    <div style={styles.wrapper}>
      <div
        style={{
          ...styles.spinner,
          width: size,
          height: size,
          borderWidth: size / 10,
        }}
      />
      {message && <p style={styles.message}>{message}</p>}
    </div>
  )
}

const styles: Record<string, React.CSSProperties> = {
  wrapper: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    gap: '0.75rem',
    padding: '2rem',
  },
  spinner: {
    border: '4px solid var(--color-border)',
    borderTopColor: 'var(--color-primary)',
    borderRadius: '50%',
    animation: 'spin 0.7s linear infinite',
  },
  message: { color: 'var(--color-muted)', fontSize: '0.9rem' },
}
