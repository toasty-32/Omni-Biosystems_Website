interface ErrorBannerProps {
  message: string
  onRetry?: () => void
}

export default function ErrorBanner({ message, onRetry }: ErrorBannerProps) {
  return (
    <div style={styles.banner}>
      <span style={styles.text}>{message}</span>
      {onRetry && (
        <button onClick={onRetry} style={styles.button}>
          Retry
        </button>
      )}
    </div>
  )
}

const styles: Record<string, React.CSSProperties> = {
  banner: {
    display: 'flex',
    alignItems: 'center',
    gap: '1rem',
    background: '#fef2f2',
    border: '1px solid #fecaca',
    borderRadius: 'var(--radius)',
    padding: '0.875rem 1.25rem',
    color: 'var(--color-error)',
    fontSize: '0.9rem',
  },
  text: { flex: 1 },
  button: {
    background: 'none',
    border: '1px solid var(--color-error)',
    borderRadius: 'var(--radius)',
    color: 'var(--color-error)',
    padding: '0.3rem 0.75rem',
    fontSize: '0.85rem',
    cursor: 'pointer',
  },
}
